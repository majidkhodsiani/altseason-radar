from datetime import datetime


def daily_report():
    now = datetime.now()

    report = f"""
📊 گزارش Altseason Radar

زمان:
{now.strftime("%Y-%m-%d %H:%M")}

وضعیت:
در حال آماده‌سازی تحلیل...

"""

    return report


if __name__ == "__main__":
    print(daily_report())
