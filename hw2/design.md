# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

In a list of dictionaries, each dictionary represent an artwork with details like title, year,artist and medium. However, if using one big dictionary, each artwork would need to have a unique key. It could makes us easy to find certain artwork by a specific key but difficult to loop through all artwork for details.

## 2. Which fields are sometimes missing? What should the app show when they are?

Somtimes missing year, medium or artist. The app would not show an error but maybe show something like "Unknown".