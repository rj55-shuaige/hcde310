# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

This is a website for university students to quickly find artworks related to their coursework using real artworks from the Art Institute of Chicago. Users can search for artworks by subject or course category, comment on and rate each artwork, compare the details of two or more artworks, save and share artworks, and give coins or upvotes. Each week, the artwork with the highest rating will be featured as the main image on the website. Give me a text sketch for the web main page, artwork detail page and compare page.

**AI's reply:**

┌──────────────────────────────────────────────────────────────┐
│                       ART COURSE                             │
│ Home        Explore        Compare        My Collection      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│          Find Artworks for Your Coursework                   │
│                                                              │
│        [ Search artworks, artists, topics... ] [Search]      │
│                                                              │
│  Browse by Subject                                           │
│                                                              │
│  [Art History] [History] [Literature] [Religion]             │
│  [Design]      [Culture] [Architecture] [Others]             │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                    ARTWORK OF THE WEEK                       │
│                                                              │
│        ┌─────────────────────────────┐                       │
│        │                             │                       │
│        │        Artwork Image        │                       │
│        │                             │                       │
│        └─────────────────────────────┘                       │
│                                                              │
│        Nude with Cats                                        │
│        Pablo Picasso · 1901                                  │
│        ★ 4.8     👍 326 helpful votes                        │
│                                                              │
│        [Save]   [Share]   [View Details]                     │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│ Search Results                                               │
│                                                              │
│ Filter: [Subject ▼] [Date ▼] [Artist ▼] [Medium ▼]          │
│                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐     │
│  │    IMAGE     │   │    IMAGE     │   │    IMAGE     │     │
│  │              │   │              │   │              │     │
│  ├──────────────┤   ├──────────────┤   ├──────────────┤     │
│  │ Artwork A    │   │ Artwork B    │   │ Artwork C    │     │
│  │ Artist       │   │ Artist       │   │ Artist       │     │
│  │ ★ 4.8        │   │ ★ 4.6        │   │ ★ 4.4        │     │
│  │ ♡ Save       │   │ ♡ Save       │   │ ♡ Save       │     │
│  │ □ Compare    │   │ □ Compare    │   │ □ Compare    │     │
│  └──────────────┘   └──────────────┘   └──────────────┘     │
│                                                              │
│                       [Compare Selected]                      │
└──────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────┐
│ ARTWORK DETAILS                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────┐    Nude with Cats                │
│  │                        │    Pablo Picasso                  │
│  │      ARTWORK IMAGE     │    1901                          │
│  │                        │                                  │
│  └────────────────────────┘    Medium: Oil on canvas         │
│                                Origin: France                │
│                                Department: Painting          │
│                                                              │
│                                ★ 4.8                         │
│                                                              │
│  [♡ Save]   [👍 Helpful]   [Share]   [+ Compare]             │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│ Comments                                                     │
│                                                              │
│ [ Write a comment...                              ] [Post]    │
│                                                              │
│ ★★★★★                                                       │
│ "Useful for my art history essay."                           │
│                                                              │
│ ★★★★☆                                                       │
│ "Interesting example for comparing modern art."              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────┐
│                    COMPARE ARTWORKS                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│        Artwork 1                    Artwork 2                 │
│                                                              │
│   ┌───────────────┐             ┌───────────────┐            │
│   │     IMAGE     │             │     IMAGE     │            │
│   └───────────────┘             └───────────────┘            │
│                                                              │
│   Nude with Cats                Cat Making Up                 │
│   Pablo Picasso                 Inagaki Tomoo                 │
│   1901                          1962                           │
│                                                              │
├───────────────────────┬──────────────────────────────────────┤
│ Medium                │ Oil on canvas | Woodblock print      │
│ Date                  │ 1901          | 1962                 │
│ Place                 │ France        | Japan                │
│ Subject               │ Human / Cats  | Cat                  │
│ Department            │ Painting      | Prints               │
├───────────────────────┴──────────────────────────────────────┤
│                                                              │
│ Your Comparison Notes                                        │
│                                                              │
│ [                                                           ]│
│ [                                                           ]│
│ [                                                           ]│
│                                                              │
│                         [Save Comparison]                     │
└──────────────────────────────────────────────────────────────┘
### Prompt 2


Build a single-page interactive website. Using the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. It's for college students who want to search related artworts for their coursework. My sketch is attached below please strictly follow it. 

**AI's reply:**

I built the app as a single HTML file. Download it and open it in a browser with an internet connection. I haven't run it against the live API, so check that the filters behave as expected.
