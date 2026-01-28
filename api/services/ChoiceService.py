from django.db import transaction
from django.shortcuts import get_object_or_404

from api.models import Choice


class ChoiceService:

    @staticmethod
    @transaction.atomic
    def vote_choice(*, choice_id: int) -> Choice:
        """
        Business logic:
        - lock row
        - increase vote
        """
        choice = get_object_or_404(
            Choice.objects.select_for_update(),
            pk=choice_id
        )

        choice.votes += 1
        choice.save(update_fields=["votes"])

        return choice