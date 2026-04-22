# Stock Project Configuration
# Contains stock symbols, company information, and metadata

stock_symbols = {
    "TCS.NS": {
        "name": "Tata Consultancy Services",
        "founder": "J. R. D. Tata",
        "history": "Founded in 1968, TCS is a part of the Tata Group and is India's largest IT services company.",
        "present_condition": "TCS remains a leading global IT services company, ranked among the top technology providers worldwide."
    },
    "INFY.NS": {
        "name": "Infosys Limited",
        "founder": "N. R. Narayana Murthy",
        "history": "Founded in 1981, Infosys pioneered the Indian IT outsourcing model and revolutionized software exports.",
        "present_condition": "Infosys is a top IT company in India with strong global presence in consulting and technology services."
    },
    "RELIANCE.NS": {
        "name": "Reliance Industries",
        "founder": "Dhirubhai Ambani",
        "history": "Reliance started in 1966 as a textiles business and expanded into petrochemicals, telecom, and retail.",
        "present_condition": "Reliance is India's largest private sector company, leading in energy, telecom, and retail sectors."
    },
    "HDFCBANK.NS": {
        "name": "HDFC Bank",
        "founder": "Hasmukhbhai Parekh",
        "history": "HDFC Bank was incorporated in 1994 and became a key player in India's banking industry.",
        "present_condition": "HDFC Bank is one of the largest private sector banks in India, offering financial services to millions."
    },
    "ICICIBANK.NS": {
        "name": "ICICI Bank",
        "founder": "ICICI Group",
        "history": "Founded in 1994, ICICI Bank has been a leader in technological advancements in banking.",
        "present_condition": "ICICI Bank continues to dominate the banking sector, focusing on retail and corporate banking."
    },
    "SBIN.NS": {
        "name": "State Bank of India",
        "founder": "British India",
        "history": "Established in 1955, SBI evolved from the Imperial Bank of India and is the largest public sector bank in India.",
        "present_condition": "SBI is the backbone of India's banking system with a massive customer base and digital outreach."
    },
    "WIPRO.NS": {
        "name": "Wipro Limited",
        "founder": "M.H. Hasham Premji",
        "history": "Founded in 1945, Wipro began as a vegetable oil manufacturer before transitioning to IT services.",
        "present_condition": "Wipro is now one of India's top IT services firms with global presence."
    },
    "HCLTECH.NS": { 
        "name": "HCL Technologies",
        "founder": "Shiv Nadar",
        "history": "HCL was established in 1976 as a hardware company, later evolving into a global IT services firm.",
        "present_condition": "HCL continues to innovate in IT services, products, and consulting."
    },
    "BHARTIARTL.NS": {
        "name": "Bharti Airtel",
        "founder": "Sunil Bharti Mittal",
        "history": "Founded in 1995, Airtel is one of the leading telecom operators in India.",
        "present_condition": "Airtel provides broadband, mobile, and digital TV services globally."
    },
    "ITC.NS": {
        "name": "ITC Limited",
        "founder": "British American Tobacco Company",
        "history": "Established in 1910, ITC started as a tobacco company and later diversified.",
        "present_condition": "ITC operates in FMCG, hotels, paperboards, and agriculture."
    },
    "LT.NS": {
        "name": "Larsen & Toubro",
        "founder": "Henning Holck-Larsen and Søren Kristian Toubro",
        "history": "Founded in 1938, L&T is an Indian multinational engaged in EPC projects and high-tech manufacturing.",
        "present_condition": "L&T is a leader in engineering, construction, and financial services."
    },
    "ASIANPAINT.NS": {
        "name": "Asian Paints",
        "founder": "Champaklal H. Choksey and partners",
        "history": "Founded in 1942, Asian Paints grew to become India's largest and Asia's third-largest paint company.",
        "present_condition": "Asian Paints leads in decorative and industrial coatings."
    },
    "MARUTI.NS": {
        "name": "Maruti Suzuki",
        "founder": "Government of India (with Suzuki collaboration)",
        "history": "Founded in 1981, Maruti revolutionized Indian car manufacturing.",
        "present_condition": "Maruti is India's leading automobile manufacturer."
    },
    "TITAN.NS": {
        "name": "Titan Company",
        "founder": "Tata Group and TIDCO",
        "history": "Established in 1984, Titan started with watches and expanded to jewelry and eyewear.",
        "present_condition": "Titan dominates India's lifestyle product market."
    },
    "BAJAJFINSV.NS": {
        "name": "Bajaj Finserv",
        "founder": "Bajaj Group",
        "history": "Founded in 2007, Bajaj Finserv focuses on financial services and insurance.",
        "present_condition": "Bajaj Finserv is a leader in India's financial sector."
    },
    "ADANIGREEN.NS": {
        "name": "Adani Green Energy",
        "founder": "Adani Group",
        "history": "Established in 2015, Adani Green specializes in renewable energy projects.",
        "present_condition": "It is one of the largest renewable energy companies in India."
    },
    "COALINDIA.NS": {
        "name": "Coal India Limited",
        "founder": "Government of India",
        "history": "Founded in 1975, Coal India is the largest coal producer in the world.",
        "present_condition": "Coal India plays a pivotal role in India's energy production."
    },
    "ULTRACEMCO.NS": {
        "name": "UltraTech Cement",
        "founder": "Birla Group",
        "history": "Established in 1983, UltraTech is a leader in cement manufacturing.",
        "present_condition": "UltraTech is India's largest cement manufacturer."
    },
    "SUNPHARMA.NS": {
        "name": "Sun Pharmaceutical",
        "founder": "Dilip Shanghvi",
        "history": "Founded in 1983, Sun Pharma started with a focus on psychiatry products.",
        "present_condition": "Sun Pharma is now India's largest pharmaceutical company."
    },
    "BAJAJ-AUTO.NS": {
        "name": "Bajaj Auto",
        "founder": "Jamnalal Bajaj",
        "history": "Established in 1945, Bajaj Auto revolutionized two-wheeler manufacturing.",
        "present_condition": "Bajaj Auto is a leading manufacturer of motorcycles and scooters globally."
    }
}

# Application Configuration
APP_CONFIG = {
    "title": "Stock Data Analyzer",
    "icon": "📊",
    "layout": "wide",
    "page_title": "Stock Price Prediction"
}

# Model Configuration
MODEL_CONFIG = {
    "arima": {
        "order": (5, 1, 0),  # p=5, d=1, q=0
        "forecast_steps": 30
    },
    "lstm": {
        "time_steps": 60,
        "units": 50,
        "epochs": 10,
        "batch_size": 32
    }
} 