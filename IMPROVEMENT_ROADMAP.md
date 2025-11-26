# 🚀 Project Improvement Roadmap

This document outlines the plan to implement all suggested improvements for the AI Trip Planner.

## 📦 Phase 1: Immediate Value (UX & Utility)
- [x] **Weather Widget**: Display current weather for the destination using Open-Meteo API (Free, No Key). ✅
- [x] **Booking/Search Links**: Add "Search on Google/Maps" buttons for every activity and hotel in the itinerary. ✅
- [ ] **PDF Export**: Allow users to download their itinerary as a beautifully formatted PDF. ⏭️ (Skipped for now)

## 🗺️ Phase 2: Enhanced Visualization (Maps)
- [x] **Interactive Maps (Leaflet.js)**: Replace static iframe with interactive map. ✅
- [ ] **Activity Markers**: Plot specific locations from the itinerary on the map.
- [ ] **Daily Routes**: Draw lines connecting activities for each day.

## 🧠 Phase 3: AI & Personalization
- [x] **"Refine Trip" Chat**: Add a chat interface on the Trip Result page to modify the itinerary (e.g., "Make it cheaper"). ✅
- [x] **Context-Awareness**: Use `UserActivity` history to influence new trip generation prompts. ✅

## 👥 Phase 4: Social & Collaboration
- [ ] **Trip Chat Rooms**: Automatically create a private chat room for each trip.
- [ ] **Shareable Links**: Generate public read-only links for itineraries.
- [ ] **"Fork" Trip**: Allow users to clone public trips.

## 📱 Phase 5: Technical & Mobile
- [ ] **PWA Support**: Add `manifest.json` and service workers for offline access.
- [ ] **Image Caching**: Optimize destination image loading.
