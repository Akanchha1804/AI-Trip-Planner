from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Trip, ChatRoom, Message
from .serializers import TripSerializer, ChatRoomSerializer, MessageSerializer
import openai
from django.conf import settings
import json

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['post'])
    def generate_itinerary(self, request, pk=None):
        trip = self.get_object()
        
        # Check if OpenAI key is valid (not placeholder)
        api_key = getattr(settings, 'OPENAI_API_KEY', None)
        use_openai = api_key and api_key != 'your_openai_key' and not api_key.startswith('your_')
        
        if not use_openai:
            # Fallback mock itinerary
            # Destination-specific detailed itineraries (7+ days each)
            destination_itineraries = {
                'Paris': [
                    ("Iconic Paris", ["Visit the Eiffel Tower (book tickets in advance)", "Walk along the Champs-Élysées", "Lunch at a traditional Parisian bistro", "Explore the Arc de Triomphe", "Evening Seine River cruise"]),
                    ("Art and Culture", ["Morning at the Louvre Museum (see Mona Lisa)", "Stroll through Tuileries Garden", "Visit Notre-Dame Cathedral (exterior)", "Explore the Latin Quarter", "Dinner in Le Marais district"]),
                    ("Montmartre & Versailles", ["Visit Sacré-Cœur Basilica in Montmartre", "Explore artist square Place du Tertre", "Afternoon trip to Palace of Versailles", "Tour the Hall of Mirrors", "Return for dinner near Opera Garnier"]),
                    ("Museums & Gardens", ["Visit Musée d'Orsay for Impressionist art", "Walk through Luxembourg Gardens", "Explore Rodin Museum and sculpture garden", "Visit Sainte-Chapelle stained glass", "Evening at Moulin Rouge cabaret show"]),
                    ("Modern Paris", ["Explore La Défense business district", "Visit Centre Pompidou modern art", "Lunch in Canal Saint-Martin area", "Shopping at Galeries Lafayette", "Sunset from Montparnasse Tower"]),
                    ("Hidden Gems", ["Morning at Père Lachaise Cemetery", "Explore Le Marais vintage shops", "Visit Musée Picasso", "Afternoon at Jardin des Plantes", "Dinner cruise on the Seine"]),
                    ("Day Trips", ["Day trip to Giverny (Monet's Gardens)", "Visit Château de Fontainebleau", "Wine tasting in Champagne region", "Return to Paris for farewell dinner", "Evening walk along the Seine"])
                ],
                'Tokyo': [
                    ("Modern Tokyo", ["Visit Senso-ji Temple in Asakusa", "Explore Akihabara electronics district", "Lunch at a conveyor belt sushi restaurant", "See Shibuya Crossing and Hachiko statue", "Evening in Shinjuku's neon streets"]),
                    ("Traditional Culture", ["Morning at Meiji Shrine", "Walk through Harajuku's Takeshita Street", "Visit teamLab Borderless digital art museum", "Explore Odaiba waterfront", "Dinner at an izakaya in Roppongi"]),
                    ("Mount Fuji Day Trip", ["Early morning trip to Mount Fuji (5th Station)", "Visit Lake Kawaguchi for views", "Lunch with Mt. Fuji view", "Explore Oshino Hakkai village", "Return to Tokyo evening"]),
                    ("Imperial & Gardens", ["Visit Imperial Palace East Gardens", "Explore Ginza shopping district", "Lunch at Tsukiji Outer Market", "Visit Tokyo Tower", "Evening in Roppongi Hills"]),
                    ("Anime & Pop Culture", ["Explore Nakano Broadway mall", "Visit Ghibli Museum (book ahead)", "Lunch in themed café", "Akihabara maid café experience", "Evening karaoke in Shibuya"]),
                    ("Traditional Tokyo", ["Morning at Tsukiji Fish Market", "Visit Ueno Park and museums", "Explore Yanaka old town", "Traditional tea ceremony", "Dinner in Asakusa"]),
                    ("Shopping & Farewell", ["Morning at Shibuya 109", "Visit Yoyogi Park", "Shopping in Omotesando", "Visit Tokyo Skytree", "Farewell dinner at teppanyaki restaurant"])
                ],
                'New York': [
                    ("Manhattan Highlights", ["Visit Statue of Liberty and Ellis Island", "Walk through Battery Park", "Explore Wall Street and Charging Bull", "Visit 9/11 Memorial and Museum", "Evening in Times Square"]),
                    ("Museums & Central Park", ["Morning at Metropolitan Museum of Art", "Walk through Central Park", "Visit Strawberry Fields (John Lennon Memorial)", "Explore Museum of Natural History", "Dinner in Upper West Side"]),
                    ("Brooklyn & Views", ["Walk across Brooklyn Bridge", "Explore DUMBO neighborhood", "Visit Brooklyn Heights Promenade", "Lunch at Smorgasburg food market", "Evening at Top of the Rock"]),
                    ("Midtown Manhattan", ["Visit Rockefeller Center", "Explore Fifth Avenue shopping", "Visit New York Public Library", "See Grand Central Terminal", "Broadway show in evening"]),
                    ("Downtown & SoHo", ["Explore SoHo art galleries", "Visit Little Italy and Chinatown", "Lunch at Chelsea Market", "Walk the High Line park", "Evening in Greenwich Village"]),
                    ("Upper East Side", ["Visit Guggenheim Museum", "Explore Museum Mile", "Lunch at Central Park Boathouse", "Visit Frick Collection", "Dinner on Upper East Side"]),
                    ("Farewell NYC", ["Morning at One World Observatory", "Visit Chelsea galleries", "Shopping in Meatpacking District", "Visit MoMA", "Farewell dinner in Tribeca"])
                ],
                'Dubai': [
                    ("Modern Marvels", ["Visit Burj Khalifa (book At The Top tickets)", "Explore Dubai Mall and aquarium", "Watch Dubai Fountain show", "Visit Dubai Frame", "Evening at Dubai Marina"]),
                    ("Culture & Souks", ["Morning at Jumeirah Mosque", "Explore Gold and Spice Souks", "Visit Dubai Museum in Al Fahidi Fort", "Abra boat ride across Dubai Creek", "Dinner at Madinat Jumeirah"]),
                    ("Desert Adventure", ["Morning desert safari with dune bashing", "Camel riding and sandboarding", "Traditional Bedouin camp lunch", "Quad biking in desert", "Evening BBQ dinner with entertainment"]),
                    ("Beach & Atlantis", ["Morning at Jumeirah Beach", "Visit Atlantis The Palm", "Aquaventure Waterpark", "Lunch at Palm Jumeirah", "Evening at La Mer beach"]),
                    ("Modern Dubai", ["Visit Museum of the Future", "Explore Dubai Design District", "Lunch at City Walk", "Visit Miracle Garden", "Evening at Global Village"]),
                    ("Abu Dhabi Day Trip", ["Day trip to Abu Dhabi", "Visit Sheikh Zayed Grand Mosque", "Explore Louvre Abu Dhabi", "Drive along Corniche", "Return to Dubai evening"]),
                    ("Shopping & Farewell", ["Morning at Mall of the Emirates", "Visit Ski Dubai", "Lunch at Kite Beach", "Sunset at Burj Al Arab", "Farewell dinner at Burj Khalifa"])
                ],
                'Bali': [
                    ("Ubud Culture", ["Visit Tegallalang Rice Terraces", "Explore Ubud Monkey Forest", "Lunch overlooking rice paddies", "Visit Ubud Royal Palace", "Traditional Balinese dance performance"]),
                    ("Temples & Waterfalls", ["Sunrise at Tanah Lot Temple", "Visit Tegenungan Waterfall", "Explore Tirta Empul water temple", "Coffee plantation tour", "Sunset at Uluwatu Temple with Kecak dance"]),
                    ("Beach Day Seminyak", ["Morning at Seminyak Beach", "Surfing lesson or beach yoga", "Lunch at beach club", "Shopping in Seminyak boutiques", "Sunset cocktails at beach bar"]),
                    ("Nature & Adventure", ["Early morning Mount Batur sunrise trek", "Breakfast with volcano view", "Visit hot springs", "Afternoon at Bali Swing", "Dinner in Ubud"]),
                    ("East Bali Exploration", ["Visit Tirta Gangga water palace", "Explore Lempuyang Temple (Gates of Heaven)", "Lunch with Agung volcano view", "Visit Taman Ujung water palace", "Return via scenic route"]),
                    ("Spa & Wellness", ["Morning yoga session", "Traditional Balinese massage", "Healthy lunch at organic café", "Visit Campuhan Ridge Walk", "Meditation and sunset viewing"]),
                    ("Beach & Farewell", ["Morning at Nusa Dua beach", "Snorkeling or water sports", "Lunch at Jimbaran Bay", "Last-minute shopping", "Farewell seafood dinner on beach"])
                ],
                'London': [
                    ("Royal London", ["Visit Buckingham Palace (Changing of Guard)", "Walk through St. James's Park", "Explore Westminster Abbey", "See Big Ben and Houses of Parliament", "Evening walk along South Bank"]),
                    ("Museums & Markets", ["Morning at British Museum", "Explore Covent Garden market", "Visit National Gallery in Trafalgar Square", "Walk through Leicester Square", "West End theatre show"]),
                    ("Tower & East London", ["Visit Tower of London and Crown Jewels", "Walk across Tower Bridge", "Explore Borough Market for lunch", "Visit Tate Modern art gallery", "Evening in Shoreditch"]),
                    ("Kensington & Hyde Park", ["Visit Kensington Palace", "Explore Hyde Park and Serpentine", "Lunch in Notting Hill", "Visit Victoria and Albert Museum", "Shopping on King's Road"]),
                    ("Camden & North London", ["Explore Camden Market", "Visit Regent's Park and Zoo", "Lunch in Primrose Hill", "Tour Abbey Road Studios area", "Evening in King's Cross"]),
                    ("Greenwich Day Trip", ["Visit Royal Observatory Greenwich", "Explore Greenwich Market", "See Cutty Sark ship", "Lunch with Thames view", "Return via Thames River cruise"]),
                    ("Shopping & Farewell", ["Morning at Harrods", "Explore Oxford Street shopping", "Visit Sky Garden for views", "Ride the London Eye", "Farewell dinner in Covent Garden"])
                ]
            }
            
            destination_name = trip.destination
            day_templates = destination_itineraries.get(destination_name, [
                ("Arrival Day", [f"Arrive in {trip.destination} and check into hotel", "Explore neighborhood around accommodation", "Visit welcome center for maps and info", "Dinner at recommended local restaurant", "Rest and prepare for adventures"]),
                ("Main Attractions", ["Visit the city's most famous landmark", "Explore the historic old town", "Lunch at traditional restaurant", "Visit main museum or cultural site", "Evening stroll through city center"]),
                ("Cultural Immersion", ["Morning at local market", "Join a walking food tour", "Visit art gallery or museum", "Explore local neighborhoods", "Dinner at authentic local spot"]),
                ("Day Trip", ["Day trip to nearby attraction", "Explore surrounding countryside", "Lunch at scenic location", "Visit historical site", "Return to city for dinner"]),
                ("Shopping & Leisure", ["Morning at main shopping district", "Visit local artisan shops", "Lunch at trendy café", "Relax at city park or garden", "Evening at popular entertainment area"]),
                ("Hidden Gems", ["Explore off-the-beaten-path locations", "Visit local favorite spots", "Lunch at neighborhood restaurant", "Discover street art or murals", "Evening at local bar or venue"]),
                ("Farewell Day", ["Last-minute sightseeing", "Shopping for souvenirs", "Visit favorite spot one more time", "Pack and prepare for departure", "Farewell dinner at special restaurant"])
            ])
            
            days_count = (trip.end_date - trip.start_date).days + 1
            mock_days = []
            
            # Generate days with variations to avoid exact repetition
            for i in range(days_count):
                template_index = i % len(day_templates)
                day_template = day_templates[template_index]
                
                # Add variation suffix for repeated cycles
                cycle_number = i // len(day_templates)
                title_suffix = f" (Extended)" if cycle_number > 0 else ""
                
                # Extract keyword for image from title
                title = day_template[0]
                image_keyword = title.split()[0].lower()  # First word of title
                
                mock_days.append({
                    "day": i + 1,
                    "title": day_template[0] + title_suffix,
                    "activities": day_template[1],
                    "image_keyword": image_keyword  # Add keyword for photo matching
                })
            
            # Destination-specific packing suggestions
            packing_suggestions = {
                'Paris': [
                    "Stylish walking shoes or loafers",
                    "Light cardigan or blazer",
                    "Jeans and dress pants",
                    "Button-down shirts or blouses",
                    "Scarf (essential Parisian accessory)",
                    "Umbrella (for unexpected rain)",
                    "Camera with extra battery",
                    "Power adapter (Type C/E plugs)",
                    "Crossbody bag or small backpack",
                    "Sunglasses and sunscreen"
                ],
                'Tokyo': [
                    "Comfortable sneakers for walking",
                    "Light layers (T-shirts, long sleeves)",
                    "Jeans or casual pants",
                    "Light rain jacket",
                    "Portable WiFi device or SIM card",
                    "Cash wallet (many places cash-only)",
                    "Face masks (common courtesy)",
                    "Compact umbrella",
                    "Power adapter (Type A/B plugs)",
                    "Small day backpack"
                ],
                'New York': [
                    "Comfortable walking sneakers",
                    "Layered clothing (weather changes quickly)",
                    "Jeans and casual pants",
                    "Light jacket or hoodie",
                    "Crossbody bag (keep hands free)",
                    "Reusable water bottle",
                    "Portable phone charger",
                    "Sunglasses and baseball cap",
                    "Metro card holder",
                    "Comfortable socks"
                ],
                'Dubai': [
                    "Lightweight breathable clothing",
                    "Modest attire for religious sites",
                    "Sandals and comfortable walking shoes",
                    "Sunglasses and wide-brim hat",
                    "High SPF sunscreen",
                    "Light scarf or shawl",
                    "Swimwear for hotel pools",
                    "Power adapter (Type G plugs)",
                    "Reusable water bottle",
                    "Light cardigan for air-conditioned malls"
                ],
                'Bali': [
                    "Flip-flops and water shoes",
                    "Light cotton t-shirts and tank tops",
                    "Shorts and light pants",
                    "Swimwear and beach cover-up",
                    "Sarong (for temple visits)",
                    "Mosquito repellent",
                    "Waterproof phone case",
                    "High SPF sunscreen",
                    "Light rain jacket",
                    "Small daypack for excursions"
                ],
                'London': [
                    "Waterproof jacket or trench coat",
                    "Comfortable walking shoes (waterproof)",
                    "Layered clothing (sweaters, cardigans)",
                    "Jeans and casual trousers",
                    "Compact umbrella",
                    "Scarf and light gloves",
                    "Power adapter (Type G plugs)",
                    "Oyster card holder",
                    "Crossbody bag",
                    "Warm socks"
                ]
            }
            
            destination_name = trip.destination
            packing_list = packing_suggestions.get(destination_name, [
                "Comfortable walking shoes",
                "T-shirts and casual tops",
                "Pants and shorts",
                "Light jacket",
                "Camera or smartphone",
                "Power bank and chargers",
                "Travel documents",
                "Sunscreen and sunglasses",
                "Reusable water bottle",
                "Basic first-aid kit"
            ])
            
            mock_itinerary = {
                "days": mock_days,
                "packing_list": packing_list,
                "mood_board_keywords": [
                    f"{trip.destination} landmarks",
                    "local cuisine",
                    "street scenes",
                    "cultural sites",
                    "sunset views"
                ]
            }
            trip.itinerary = json.dumps(mock_itinerary)
            trip.save()
            return Response({'status': 'itinerary generated', 'itinerary': trip.itinerary})

        # Use OpenAI if key is valid
        openai.api_key = api_key
        
        try:
            days_count = (trip.end_date - trip.start_date).days + 1
            prompt = f"""
            Generate a {days_count} day trip itinerary for {trip.destination} with a budget of ${trip.budget}.
            Return ONLY a valid JSON object with the following structure:
            {{
                "days": [
                    {{
                        "day": 1,
                        "title": "Theme of the day",
                        "activities": ["Activity 1", "Activity 2", "Activity 3", "Activity 4"]
                    }}
                ],
                "packing_list": ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
                "mood_board_keywords": ["Keyword 1", "Keyword 2", "Keyword 3"]
            }}
            """
            
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful travel assistant that generates structured JSON itineraries."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = response.choices[0].message.content
            trip.itinerary = content
            trip.save()
            return Response({'status': 'itinerary generated', 'itinerary': content})
            
        except Exception as e:
            print(f"OpenAI Error: {e}")
            # Fallback to mock on error
            mock_itinerary = {
                "days": [
                    {
                        "day": 1,
                        "title": "Arrival and Exploration",
                        "activities": [f"Arrive in {trip.destination}", "Check into hotel", "Evening walk", "Dinner"]
                    }
                ],
                "packing_list": ["Comfortable shoes", "Camera", "Charger"],
                "mood_board_keywords": [f"{trip.destination}", "travel", "adventure"]
            }
            trip.itinerary = json.dumps(mock_itinerary)
            trip.save()
            return Response({'status': 'itinerary generated (fallback)', 'itinerary': trip.itinerary})

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    @action(detail=False, methods=['post'])
    def join_private(self, request):
        code = request.data.get('room_code')
        try:
            room = ChatRoom.objects.get(room_code=code, is_private=True)
            return Response(ChatRoomSerializer(room).data)
        except ChatRoom.DoesNotExist:
            return Response({'error': 'Invalid room code'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get', 'post'])
    def messages(self, request, pk=None):
        room = self.get_object()
        if request.method == 'GET':
            messages = room.messages.all()
            return Response(MessageSerializer(messages, many=True).data)
        elif request.method == 'POST':
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(room=room)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
