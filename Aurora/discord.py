import requests

# ฟังก์ชันดึงข้อมูลผู้ใช้
def get_user_data(token):
    headers = {"Authorization": token}
    try:
        response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return [
                data.get("username"),
                data.get("discriminator"),
                data.get("email"),
                data.get("phone")
            ]
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def has_payment_methods(token):
    headers = {"Authorization": token}
    try:
        response = requests.get(
            "https://discord.com/api/v10/users/@me/billing/payment-sources",
            headers=headers
        )
        return response.status_code == 200 and len(response.json()) > 0
    except Exception as e:
        print(f"Error: {e}")
        return False