from datetime import date, timedelta

from .models import Member, Notification


def generate_birthday_notifications():

    today = date.today()

    tomorrow = today + timedelta(days=1)

    members = Member.objects.all()

    for member in members:

        # Birthday today
        if (
            member.birthday.month == today.month
            and
            member.birthday.day == today.day
        ):

            if member.user:

                Notification.objects.get_or_create(

                    recipient=member.user,

                    title="🎂 Happy Birthday!",

                    defaults={

                    "message": f"Happy Birthday, {member.full_name}! May God bless you abundantly.",

                    "notification_type": "birthday",

    }

)

        # Birthday tomorrow
        elif (
            member.birthday.month == tomorrow.month
            and
            member.birthday.day == tomorrow.day
        ):

            if member.user:
                Notification.objects.get_or_create(

                    recipient=member.user,

                    title="🎂 Happy Birthday!",

                    defaults={

                    "message": f"Happy Birthday, {member.full_name}! May God bless you abundantly.",

                    "notification_type": "birthday",

    }

)