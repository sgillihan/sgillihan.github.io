"""
Project Dictionary for Proxy Data Project (CSPB 3112)
Sortable by term (alphabetical) or by category.
"""

TERMS = [
    {
        "term": "Affordances",
        "abbreviation": None,
        "category": "General",
        "definition": (
            "The perceived and actual properties of something that determines how it might be used "
            "(as pioneered by James Gibson)."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "ARIMA",
        "abbreviation": "AutoRegressive Integrated Moving Average",
        "category": "ML: Time Series & Sequential",
        "definition": (
            "Widely used statistical method for analyzing and forecasting time-ordered data, "
            "including stock prices, sales, and weather patterns. Uses past values (autoregression) "
            "and past forecast errors (moving average) to predict future data, handling "
            "non-stationary trends by differentiating data (integration)."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Bayesian Improved Surname Geocoding (BISG)",
        "abbreviation": "BISG",
        "category": "ML: Location & Geospatial",
        "definition": (
            "An algorithm that combines a user's geographic location (zip code/census tract) with "
            "their surname to infer race, ethnicity, or socioeconomic status."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Centrality Measures",
        "abbreviation": None,
        "category": "ML: Graph & Network Analysis",
        "definition": (
            "Network analysis tools that quantify the importance, influence, or prominence of "
            "specific nodes (vertices) within a graph."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "CFAA",
        "abbreviation": "Computer Fraud and Abuse Act",
        "category": "Privacy & Regulation",
        "definition": (
            "The primary U.S. federal law enacted in 1986 to combat hacking and computer-related "
            "crimes. It prohibits accessing protected computers without authorization or exceeding "
            "authorized access to steal data, cause damage, or perpetrate fraud."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Clustering Algorithms (DBSCAN & K-Means)",
        "abbreviation": None,
        "category": "ML: Location & Geospatial",
        "definition": (
            "Algorithms that identify geographically concentrated 'hotspots' or frequently visited "
            "places (like a 'home' or 'work' area) to infer user demographics or routines."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Community Detection",
        "abbreviation": None,
        "category": "ML: Graph & Network Analysis",
        "definition": (
            "Algorithms that identify clusters of densely connected nodes (communities) within "
            "complex networks, separating them from sparser external connections. Used to map "
            "social networks, detect fraudulent behavior, analyze biological networks, and "
            "optimize network segmentation."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "DBSCAN",
        "abbreviation": "Density-Based Spatial Clustering of Applications with Noise",
        "category": "ML: Unsupervised Learning",
        "definition": (
            "A popular unsupervised machine learning algorithm that groups data points based on "
            "their spatial density. Does not require specifying the number of clusters in advance "
            "and can discover clusters of arbitrary shapes while effectively identifying outliers "
            "as noise. Each data point is classified as one of 3 types (core point, border point, "
            "noise point) based on 2 parameters: epsilon (search radius) and minpts (minimum "
            "points required in that radius)."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "DNS",
        "abbreviation": "Domain Name System",
        "category": "Networking & Web",
        "definition": (
            "The internet's decentralized 'phonebook' that translates human-readable domain names "
            "into numerical IP addresses needed for computers to connect. Allows users to access "
            "websites without memorizing complex numbers, utilizing a hierarchical system of "
            "servers to resolve queries."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Econometrician",
        "abbreviation": None,
        "category": "General",
        "definition": (
            "A specialized economist who uses mathematical statistics, data analysis, and economic "
            "theory to forecast economic trends, test hypotheses, and evaluate policy impacts."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Electron",
        "abbreviation": None,
        "category": "Software Frameworks",
        "definition": (
            "An open-source framework that enables developers to build cross-platform desktop "
            "applications using web technologies like JavaScript, HTML, and CSS. Maintained by the "
            "OpenJS Foundation, it allows a single codebase to run natively on macOS, Windows, and "
            "Linux by combining Chromium (frontend) and Node.js (backend) into a single runtime."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Explainability Tools (SHAP/LIME)",
        "abbreviation": None,
        "category": "ML: Explainability",
        "definition": (
            "The two most popular tools used in Explainable AI (XAI) to interpret 'black-box' "
            "machine learning models. They help make complex model decisions transparent and "
            "trustworthy by identifying which features contributed most to a prediction."
        ),
        "subtypes": [
            {
                "name": "SHAP (SHapley Additive exPlanations)",
                "description": (
                    "Based on game theory, assigning an importance value to each feature for a "
                    "particular prediction (local) or across a whole dataset (global). "
                    "High consistency, high computational cost."
                ),
            },
            {
                "name": "LIME (Local Interpretable Model-agnostic Explanations)",
                "description": (
                    "Focuses on local interpretability, creating a simple, interpretable linear "
                    "model around a single prediction to explain how the complex model behaves in "
                    "that specific area. Lower consistency, runs fast."
                ),
            },
        ],
        "url": None,
    },
    {
        "term": "FIPP",
        "abbreviation": "Fair Information Practice Principles",
        "category": "Privacy & Regulation",
        "definition": (
            "A collection of widely accepted principles that agencies use when evaluating "
            "information systems, processes, programs, and activities that affect individual "
            "privacy. The FIPPs are not requirements; rather, they are principles to be applied "
            "according to each agency's particular mission and privacy program requirements. "
            "Note: https://www.fpc.gov/resources/fipps/ is scheduled for removal 3/30/2026."
        ),
        "subtypes": [
            {"name": "Access and Amendment", "description": "Agencies should provide individuals with appropriate access to PII and appropriate opportunity to correct or amend PII."},
            {"name": "Accountability", "description": "Agencies should be accountable for complying with these principles and applicable privacy requirements, and should appropriately monitor, audit, and document compliance. Agencies should also clearly define the roles and responsibilities with respect to PII for all employees and contractors, and should provide appropriate training to all employees and contractors who have access to PII."},
            {"name": "Authority", "description": "Agencies should only create, collect, use, process, store, maintain, disseminate, or disclose PII if they have authority to do so, and should identify this authority in the appropriate notice."},
            {"name": "Minimization", "description": "Agencies should only create, collect, use, process, store, maintain, disseminate, or disclose PII that is directly relevant and necessary to accomplish a legally authorized purpose, and should only maintain PII for as long as is necessary to accomplish the purpose."},
            {"name": "Quality and Integrity", "description": "Agencies should create, collect, use, process, store, maintain, disseminate, or disclose PII with such accuracy, relevance, timeliness, and completeness as is reasonably necessary to ensure fairness to the individual."},
            {"name": "Individual Participation", "description": "Agencies should involve the individual in the process of using PII and, to the extent practicable, seek individual consent for the creation, collection, use, processing, storage, maintenance, dissemination, or disclosure of PII. Agencies should also establish procedures to receive and address individuals' privacy-related complaints and inquiries."},
            {"name": "Purpose Specification and Use Limit", "description": "Agencies should provide notice of the specific purpose for which PII is collected and should only use, process, store, maintain, disseminate, or disclose PII for a purpose that is explained in the notice and is compatible with the purpose for which the PII was collected, or that is otherwise legally authorized."},
            {"name": "Security", "description": "Agencies should establish administrative, technical, and physical safeguards to protect PII commensurate with the risk and magnitude of the harm that would result from its unauthorized access, use, modification, loss, destruction, dissemination, or disclosure."},
            {"name": "Transparency", "description": "Agencies should be transparent about information policies and practices with respect to PII, and should provide clear and accessible notice regarding creation, collection, use, processing, storage, maintenance, dissemination, and disclosure of PII."},
        ],
        "url": "https://www.fpc.gov/resources/fipps/",
    },
    {
        "term": "GDPR",
        "abbreviation": "General Data Protection Regulation",
        "category": "Privacy & Regulation",
        "definition": (
            "EU law that requires a legal basis for data processing and imposes various "
            "transparency and autonomy-enhancing safeguards."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Geohashing / Geographical Indexing",
        "abbreviation": None,
        "category": "ML: Location & Geospatial",
        "definition": (
            "Algorithms that convert precise latitude/longitude into a 'geohash' string. This acts "
            "as a coarse location proxy, allowing for targeted ads or local content without "
            "revealing a user's exact, pinpoint coordinates."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Gradient Boosting (XGBoost / LightGBM)",
        "abbreviation": None,
        "category": "ML: Supervised Learning",
        "definition": (
            "An ensemble machine learning technique that builds a strong predictive model by "
            "sequentially adding decision trees, with each new tree designed to correct the errors "
            "(residuals) of the previous ones. XGBoost and LightGBM are two of the most popular "
            "high-performance implementations."
        ),
        "subtypes": [
            {
                "name": "XGBoost (Extreme Gradient Boosting)",
                "description": (
                    "Grows trees depth first, expanding all nodes at a level before moving deeper. "
                    "Balanced, stable performance with excellent regularization to prevent overfitting. "
                    "Traditionally uses a sorted-based algorithm to find best splits. Best for "
                    "medium-sized structured data, Kaggle competitions, and fine-tuned control."
                ),
            },
            {
                "name": "LightGBM (Light Gradient Boosting Machine)",
                "description": (
                    "Grows trees by splitting the leaf that reduces loss the most, often creating "
                    "deeper and more efficient trees. Exceptional speed and memory efficiency, "
                    "especially on massive datasets. Uses a histogram-based algorithm that buckets "
                    "values into discrete bins for faster computation. Best for large-scale datasets "
                    "where training time is a critical factor."
                ),
            },
        ],
        "url": None,
    },
    {
        "term": "Hidden Markov Model (HMM)",
        "abbreviation": "HMM",
        "category": "ML: Time Series & Sequential",
        "definition": (
            "Statistical models used to predict sequences of hidden, unobservable states based on "
            "observed data. They assume a Markov process where current hidden states depend only on "
            "previous states, influencing observable outcomes. Used to infer user activity purposes "
            "(e.g., commuting, leisure) from mobility records."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Hierarchical Clustering",
        "abbreviation": None,
        "category": "ML: Unsupervised Learning",
        "definition": (
            "Unsupervised machine learning algorithm that groups similar data points into a "
            "tree-like structure called a dendrogram."
        ),
        "subtypes": [
            {
                "name": "Agglomerative Clustering",
                "description": (
                    "'Bottom-up' hierarchical algorithm where each data point starts as its own "
                    "cluster and is iteratively merged with nearest neighbor based on distance "
                    "metrics and linkage criteria until all points form a single cluster or until a "
                    "target number of clusters is reached."
                ),
            },
            {
                "name": "Divisive Clustering",
                "description": (
                    "'Top-down' approach — all data points start in a single cluster, which is "
                    "then split recursively."
                ),
            },
        ],
        "url": None,
    },
    {
        "term": "Identity Graphs (Cross-Device Targeting)",
        "abbreviation": None,
        "category": "ML: Location & Geospatial",
        "definition": (
            "Use IP address locations to link multiple devices (e.g., phone and laptop) to a "
            "single user profile."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "K-Means",
        "abbreviation": None,
        "category": "ML: Unsupervised Learning",
        "definition": (
            "Unsupervised machine learning algorithm used to group unlabeled data into k distinct, "
            "non-overlapping clusters based on feature similarity. Primarily used for finding "
            "hidden patterns within a dataset without the need for pre-defined labels. Applications: "
            "customer segmentation, image compression, anomaly detection, document clustering."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Latent Dirichlet Allocation (LDA)",
        "abbreviation": "LDA",
        "category": "ML: NLP & Text Mining",
        "definition": (
            "Probabilistic, unsupervised machine learning model that automatically discovers hidden "
            "thematic structures (topics) within text collections. Applications: recommender "
            "systems (news articles or products), sentiment/theme analysis."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Logistic Regression",
        "abbreviation": None,
        "category": "ML: Supervised Learning",
        "definition": (
            "A supervised machine learning algorithm primarily used for classification tasks. Used "
            "to predict the probability of a discrete or categorical outcome rather than a "
            "continuous value."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Long Short-Term Memory (LSTM) Networks",
        "abbreviation": "LSTM",
        "category": "ML: Time Series & Sequential",
        "definition": (
            "Neural networks frequently used to analyze time-series trajectory data (latitude, "
            "longitude, and time) to predict a user's next location."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Markov Chain Models",
        "abbreviation": None,
        "category": "ML: Location & Geospatial",
        "definition": (
            "Used in location-based social networks (LBSNs) to model the probability of moving "
            "from one location (e.g., home) to another (e.g., work)."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "MUSA",
        "abbreviation": "Mitigating Unauthorized Scraping Alliance",
        "category": "Privacy & Regulation",
        "definition": (
            "Convenes industry leaders, policymakers, and the public to advance a global dialogue "
            "on unauthorized data scraping and responsible data use. Dedicated to protecting user "
            "data through education, advocacy, public-private collaboration, and sharing of "
            "effective practices to mitigate unauthorized scraping. Seeks to establish a "
            "coordinated, unified approach to addressing unauthorized scraping and data misuse."
        ),
        "subtypes": [],
        "url": "https://antiscrapingalliance.org/",
    },
    {
        "term": "Naïve Bayes",
        "abbreviation": None,
        "category": "ML: Supervised Learning",
        "definition": (
            "A family of probabilistic machine learning classifiers based on Bayes' Theorem. "
            "Primarily used for classification tasks where the goal is to predict the category of "
            "a data point based on its features. Assumes every feature in the dataset is "
            "independent of all other features given the class. Common applications include spam "
            "filtering, sentiment analysis, document categorization, and medical diagnosis."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "PageRank",
        "abbreviation": None,
        "category": "ML: Graph & Network Analysis",
        "definition": (
            "An algorithm used by Google Search to rank web pages based on their importance, "
            "treating links as 'votes' of confidence."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "PII",
        "abbreviation": "Personally Identifiable Information",
        "category": "Privacy & Regulation",
        "definition": (
            "Refers to any data that can be used to distinguish, trace, or identify an individual's "
            "identity — such as names, Social Security numbers, or biometric records — either alone "
            "or when combined with other personal information."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Prophet",
        "abbreviation": None,
        "category": "ML: Time Series & Sequential",
        "definition": (
            "Open-source additive time-series forecasting model developed by Meta. Designed for "
            "analyzing data with strong seasonal effects and historical trends, such as daily, "
            "weekly, or yearly data. Fast, automated, robust to missing data and trend shifts, "
            "and works well with outliers."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "PySide6",
        "abbreviation": None,
        "category": "Software Frameworks",
        "definition": (
            "The official Python module from the Qt Company that provides bindings for the Qt6 "
            "framework, allowing developers to create cross-platform GUIs and applications for "
            "desktop and mobile. Acts as a wrapper enabling Python developers to utilize powerful "
            "C++ Qt6 components while building software for Windows, macOS, Linux, Android, and iOS."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Qt6",
        "abbreviation": None,
        "category": "Software Frameworks",
        "definition": (
            "A cross-platform C++ application development framework used to create high-performance "
            "GUI, desktop, mobile, and embedded software from a single codebase. Provides tools for "
            "designing 2D/3D user interfaces and desktop applications, featuring modern APIs, "
            "improved CMake support, and enhanced performance."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Random Forest",
        "abbreviation": None,
        "category": "ML: Supervised Learning",
        "definition": (
            "A popular supervised ensemble machine learning algorithm that combines the outputs of "
            "multiple decision trees to reach a single, more accurate result. Used for both "
            "classification (predicting categories) and regression (predicting continuous values)."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Request-Body Logging",
        "abbreviation": None,
        "category": "Networking & Web",
        "definition": (
            "The process of capturing and storing the payload data sent by a client to an API or "
            "server as part of an HTTP request. While standard access logs record URL, HTTP method, "
            "and status code, request-body logging provides the actual content (JSON objects, XML "
            "data, form parameters). Used for debugging/troubleshooting, security auditing, or "
            "compliance and monitoring. Significant security and privacy risks exist as request "
            "bodies often contain plain text passwords, credit card numbers, or PII. Best practices: "
            "conditional logging, redaction and sanitization, structured logging, truncation."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Sequence Mining",
        "abbreviation": None,
        "category": "ML: Unsupervised Learning",
        "definition": (
            "A data mining technique that identifies frequently occurring, ordered subsequences "
            "within larger datasets, such as purchasing behavior, DNA sequences, or web "
            "clickstreams. Discovers statistically relevant patterns where the order of events "
            "matters, often using a minimum support threshold to determine frequency."
        ),
        "subtypes": [
            {"name": "Closed Sequential Patterns", "description": "Patterns where no super-pattern has the same frequency."},
            {"name": "Maximal Sequential Patterns", "description": "A smaller set of patterns where no super-pattern is frequent."},
            {"name": "High Utility Sequential Patterns", "description": "Focuses on sequences with high significance rather than just high frequency."},
            {"name": "GSP (Generalized Sequential Pattern)", "description": "A breadth-first Apriori-based algorithm that scans the database multiple times."},
            {"name": "PrefixSpan (Prefix-projected Sequential Pattern mining)", "description": "A pattern-growth approach that avoids candidate generation by projecting databases."},
            {"name": "SPADE (Sequential Pattern Discovery using Equivalence classes)", "description": "Uses a vertical database layout to find sequences."},
        ],
        "url": None,
    },
    {
        "term": "Tauri",
        "abbreviation": None,
        "category": "Software Frameworks",
        "definition": (
            "An open-source framework for building tiny, fast, and secure cross-platform desktop "
            "and mobile applications using web technologies (HTML, CSS, JS) for the frontend and "
            "Rust for the backend. By leveraging the OS's native web renderer instead of bundling "
            "a browser engine, Tauri creates significantly smaller binaries compared to Electron."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "TF-IDF",
        "abbreviation": "Term Frequency-Inverse Document Frequency",
        "category": "ML: NLP & Text Mining",
        "definition": (
            "A statistical weighting technique used in information retrieval and text mining to "
            "evaluate how important a word is to a document within a collection. Applications: "
            "search engine ranking, keyword extraction, stop word filtering."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Tkinter",
        "abbreviation": None,
        "category": "Software Frameworks",
        "definition": (
            "The standard, built-in library for creating GUIs in the Python programming language. "
            "Provides developers with a robust, platform-independent toolkit for building desktop "
            "applications that can run on Windows, macOS, and Linux without modification."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Transformer Embeddings",
        "abbreviation": None,
        "category": "ML: NLP & Text Mining",
        "definition": (
            "Dense, high-dimensional numerical vectors that map words, tokens, or entire sentences "
            "into a semantic space where similar meanings are positioned closely together — "
            "essential for turning text into numbers that models can understand. Applications: "
            "semantic search, text classification and clustering, machine translation, "
            "image processing."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "TTL",
        "abbreviation": "Time to Live",
        "category": "Networking & Web",
        "definition": (
            "A numerical value that determines how long a data packet, network record, or cached "
            "content remains valid before it is discarded or refreshed. Prevents data from "
            "circulating indefinitely, which helps optimize network efficiency and ensures "
            "information freshness."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "\"Virtual Friend\" Algorithms (ST-LSTM)",
        "abbreviation": "ST-LSTM",
        "category": "ML: Location & Geospatial",
        "definition": (
            "Identify groups of users who not only have similar behavior patterns but are also "
            "geographically close to one another, using location to identify people with "
            "similar lifestyles."
        ),
        "subtypes": [],
        "url": None,
    },
    {
        "term": "Wrapper",
        "abbreviation": None,
        "category": "General",
        "definition": (
            "A piece of code (like a function, class, or program) that 'wraps' around another "
            "piece of software to provide a different interface or add specific functionality "
            "without modifying the original code. Can be thought of as a translator or "
            "intermediary layer."
        ),
        "subtypes": [],
        "url": None,
    },
]

# --- ML Tools Comparison Table ---
ML_TOOLS_COMPARISON = {
    "columns": ["Feature", "Scikit-learn", "XGBoost", "PyTorch"],
    "rows": [
        {
            "Feature": "Primary Use Case",
            "Scikit-learn": "Traditional/Classical ML",
            "XGBoost": "High-performance Gradient Boosting",
            "PyTorch": "Deep Learning & Custom Research",
        },
        {
            "Feature": "Core Algorithms",
            "Scikit-learn": "Regression, SVM, Random Forest, Clustering",
            "XGBoost": "eXtreme Gradient Boosting (GBDT)",
            "PyTorch": "Neural Networks, CNNs, RNNs, Transformers",
        },
        {
            "Feature": "Data Type",
            "Scikit-learn": "Structured/Tabular (Small-Medium)",
            "XGBoost": "Structured/Tabular (Large)",
            "PyTorch": "Unstructured (Images, Text, Audio)",
        },
        {
            "Feature": "Hardware Support",
            "Scikit-learn": "CPU-focused",
            "XGBoost": "CPU & GPU support",
            "PyTorch": "Heavy GPU/TPU acceleration",
        },
        {
            "Feature": "Complexity",
            "Scikit-learn": "Simple, unified API",
            "XGBoost": "Moderate; specialized parameters",
            "PyTorch": "High; requires manual architectural design",
        },
    ],
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def by_alpha():
    """Return all terms sorted alphabetically by term name."""
    return sorted(TERMS, key=lambda t: t["term"].lower().lstrip('"'))


def by_category():
    """Return a dict mapping each category to its sorted list of terms."""
    result = {}
    for entry in sorted(TERMS, key=lambda t: t["term"].lower().lstrip('"')):
        result.setdefault(entry["category"], []).append(entry)
    return result


def search(keyword: str):
    """Return all terms whose term name or definition contains the keyword (case-insensitive)."""
    kw = keyword.lower()
    return [
        t for t in TERMS
        if kw in t["term"].lower() or kw in t["definition"].lower()
    ]


def print_term(entry: dict):
    """Pretty-print a single dictionary entry."""
    abbr = f" ({entry['abbreviation']})" if entry["abbreviation"] else ""
    print(f"\n{'='*70}")
    print(f"  {entry['term']}{abbr}")
    print(f"  Category: {entry['category']}")
    print(f"{'='*70}")
    print(f"  {entry['definition']}")
    if entry["subtypes"]:
        print()
        for sub in entry["subtypes"]:
            print(f"    • {sub['name']}")
            print(f"      {sub['description']}")
    if entry["url"]:
        print(f"\n  URL: {entry['url']}")


def print_all_by_category():
    """Print the full dictionary organized by category."""
    for category, entries in sorted(by_category().items()):
        print(f"\n{'#'*70}")
        print(f"  {category.upper()}")
        print(f"{'#'*70}")
        for entry in entries:
            print_term(entry)


def print_all_alphabetical():
    """Print the full dictionary in alphabetical order."""
    for entry in by_alpha():
        print_term(entry)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "alpha":
        print_all_alphabetical()
    elif len(sys.argv) > 1 and sys.argv[1] == "search":
        keyword = " ".join(sys.argv[2:])
        results = search(keyword)
        print(f"\nFound {len(results)} result(s) for '{keyword}':")
        for entry in results:
            print_term(entry)
    else:
        print_all_by_category()
