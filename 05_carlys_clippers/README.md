# Carly's Clippers - Data Optimization Project ✂️

This project is part of my **Data Science/Engineering Career Path**. It focuses on processing hairstyle and pricing data to automate business insights and update service costs.

## 🛠️ Key Technical Skills Applied
*   **Multi-list Synchronization:** Managed three parallel data streams (`hairstyles`, `prices`, `last_week`) using index-based loops (`range(len())`).
*   **Data Transformation:** Implemented dynamic pricing updates using **List Comprehensions**.
*   **Aggregated Analytics:** Calculated total revenue and average costs through iterative accumulation.
*   **Conditional Filtering:** Designed logic to identify promotional services based on price thresholds.

## 🧠 The "Sweat & Code" Logic
One of the core challenges was synchronizing disparate lists. Instead of basic iteration, I used **index-based pointers** `[i]` to ensure that the metadata (names) stayed aligned with the transactional data (prices and sales) across the entire pipeline.

## 🚀 How to Run
1. Clone the repository.
2. Run `python script.py` in your terminal.
