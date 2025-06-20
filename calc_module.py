import re

def handle_calc(query: str) -> str:
    try:
        query = query.lower()
        if "sip" in query:
            
            match = re.search(r'(\d+)[\s-]*year', query)
            years = int(match.group(1)) if match else 5

            match = re.search(r'₹?[\s]?(\d{3,6})', query.replace(',', ''))
            monthly_invest = int(match.group(1)) if match else 10000

            rate = 0.12  # Default 12% annual return
            n = years * 12
            r = rate / 12

            future_value = monthly_invest * (((1 + r)**n - 1) * (1 + r)) / r
            return f"SIP Future Value: ₹{future_value:,.2f}"

        elif "emi" in query:
            match = re.findall(r"\d+", query)
            principal, annual_rate, years = map(int, match[:3])
            monthly_rate = annual_rate / (12 * 100)
            n = years * 12
            emi = (principal * monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
            return f"EMI per month: ₹{emi:,.2f}"

        elif "roi" in query:
            match = re.findall(r"\d+", query)
            gain, cost = map(int, match[:2])
            roi = ((gain - cost) / cost) * 100
            return f"ROI: {roi:.2f}%"

        else:
            return "Please provide a complete formula-based query (SIP/EMI/ROI)."

    except Exception as e:
        return f" Error in calculation: {str(e)}"

