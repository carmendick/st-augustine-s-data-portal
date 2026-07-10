from members.models import Member

from django.db.models import Count


def total_members():

    return Member.objects.count()


def total_states():

    return (

        Member.objects
        .values("state_residence")
        .distinct()
        .count()

    )