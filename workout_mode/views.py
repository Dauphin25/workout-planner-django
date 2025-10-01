from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import WorkoutSession, WorkoutSessionExercise

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def next_exercise(self, request, pk=None):
        session = self.get_object()
        next_ex = session.exercises.filter(is_completed=False).order_by('order').first()
        if not next_ex:
            return Response({'detail': 'All exercises completed.'})
        data = {
            'id': next_ex.id,
            'exercise_name': next_ex.exercise_name,
            'sets': next_ex.sets,
            'repetitions': next_ex.repetitions,
            'rest_seconds': next_ex.rest_seconds,
            'order': next_ex.order,
            'notes': next_ex.notes,
        }
        return Response(data)

class WorkoutSessionExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSessionExercise.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutSessionExercise.objects.filter(session__user=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        ex = self.get_object()
        ex.is_completed = True
        ex.completed_at = timezone.now()
        ex.save()
        return Response({'detail': 'Exercise marked as complete.'})

    @action(detail=True, methods=['post'])
    def adjust(self, request, pk=None):
        ex = self.get_object()
        ex.adjusted_reps = request.data.get('adjusted_reps')
        ex.adjusted_sets = request.data.get('adjusted_sets')
        ex.adjusted_rest_seconds = request.data.get('adjusted_rest_seconds')
        ex.notes = request.data.get('notes', ex.notes)
        ex.save()
        return Response({'detail': 'Adjustments saved.'})
