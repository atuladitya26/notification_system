import datetime
import random

class User:
    def __init__(self, user_id, name, device_type, device_token=None):
        self.user_id = user_id
        self.name = name
        self.device_type = device_type
        self.device_token = device_token if device_type == "mobile" else None  # Only mobile users need device tokens

class NotificationSystem:
    def __init__(self):
        self.users = []
        self.notification_logs = []
    
    def add_user(self, user):
        self.users.append(user)

    def send_notification(self, user, title, message, notification_type):
        timestamp = datetime.datetime.now()
        
        # Validate the notification type and the user's device type
        if notification_type not in ["push", "in-app"]:
            return f"Error: Invalid notification type: {notification_type}"
        
        if notification_type == "push" and user.device_type != "mobile":
            return f"Error: {user.name} is not a mobile user. Can't send push notification."
        
        if notification_type == "in-app" and user.device_type != "web":
            return f"Error: {user.name} is not a web user. Can't send in-app notification."
        
        # Simulate sending the notification (this could be a real API call in production)
        status = self.simulate_send_notification(user, title, message, notification_type)
        
        # Log the notification
        log_entry = {
            'timestamp': timestamp,
            'user': user.name,
            'notification_type': notification_type,
            'status': status,
            'message': message
        }
        self.notification_logs.append(log_entry)
        
        return f"Notification sent to {user.name} at {timestamp}. Status: {status}"

    def simulate_send_notification(self, user, title, message, notification_type):
        """Simulate the sending process of a notification."""
        # Randomly simulate success or failure
        success = random.choice([True, False])
        if success:
            return "success"
        else:
            return f"failure: Failed to send to {user.name}"
    
    def get_notification_logs(self):
        return self.notification_logs

# Example usage:

# Initialize notification system
notification_system = NotificationSystem()

# Simulate a list of users
users = [
    User(user_id=1, name="Abhi", device_type="mobile", device_token="token_123"),
    User(user_id=2, name="Birbal", device_type="web"),
    User(user_id=3, name="Chahel", device_type="mobile", device_token="token_456"),
    User(user_id=4, name="Dia", device_type="web"),
    User(user_id=5, name="Eashan", device_type="mobile", device_token="token_789")
]

# Add users to the notification system
for user in users:
    notification_system.add_user(user)

# Send push and in-app notifications
for user in notification_system.users:
    title = "New Message"
    message = "You have a new notification!"
    notification_type = "push" if user.device_type == "mobile" else "in-app"
    result = notification_system.send_notification(user, title, message, notification_type)
    print(result)

# Print the notification logs
print("\nNotification Logs:")
for log in notification_system.get_notification_logs():
    print(log)
