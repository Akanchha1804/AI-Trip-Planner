# Quick verification script for Save Trip feature
# Run this in Django shell: python manage.py shell < verify_setup.py

from trips.models import Trip, Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

print("=" * 60)
print("SAVE TRIP FEATURE - VERIFICATION")
print("=" * 60)

# Check if models exist
print("\n✓ Checking models...")
print(f"  Trip model: {Trip._meta.db_table}")
print(f"  Booking model: {Booking._meta.db_table}")

# Check if user field exists in Trip
trip_fields = [f.name for f in Trip._meta.get_fields()]
if 'user' in trip_fields:
    print("  ✅ Trip.user field exists")
else:
    print("  ❌ Trip.user field MISSING - run migrations!")

# Check users
user_count = User.objects.count()
print(f"\n✓ Users in database: {user_count}")
if user_count > 0:
    for user in User.objects.all()[:5]:
        token_exists = Token.objects.filter(user=user).exists()
        print(f"  - {user.username} (Token: {'✅' if token_exists else '❌'})")

# Check trips
trip_count = Trip.objects.count()
print(f"\n✓ Trips in database: {trip_count}")
if trip_count > 0:
    trips_with_user = Trip.objects.filter(user__isnull=False).count()
    trips_without_user = Trip.objects.filter(user__isnull=True).count()
    print(f"  - With user: {trips_with_user}")
    print(f"  - Without user: {trips_without_user}")
    
    print("\n  Recent trips:")
    for trip in Trip.objects.all().order_by('-created_at')[:5]:
        user_str = trip.user.username if trip.user else "No user"
        print(f"    {trip.id}. {trip.destination} - {user_str}")

# Check bookings
booking_count = Booking.objects.count()
print(f"\n✓ Bookings in database: {booking_count}")

print("\n" + "=" * 60)
print("RECOMMENDATIONS:")
print("=" * 60)

if user_count == 0:
    print("⚠️  No users found. Create a user:")
    print("   python manage.py createsuperuser")

if trip_count == 0:
    print("ℹ️  No trips found. Create a trip via the frontend.")

if trip_count > 0 and trips_without_user > 0:
    print(f"ℹ️  {trips_without_user} trips without users.")
    print("   These trips were created before login.")
    print("   Click 'Save Trip' while logged in to associate them.")

print("\n✅ Verification complete!")
