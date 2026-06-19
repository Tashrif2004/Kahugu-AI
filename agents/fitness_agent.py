"""Fitness Agent - Tracks workouts and health metrics"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class FitnessAgent:
    """Tracks workouts, movements, and provides fitness advice."""

    def __init__(self):
        self.name = "Fitness Agent"
        self.workout_history = []
        self.daily_stats = {}
        self.goals = {}
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process fitness command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def log_workout(self, workout_type: str, duration: int, calories: int, notes: Optional[str] = None) -> Dict[str, Any]:
        """Log a workout session."""
        workout = {
            'id': len(self.workout_history),
            'type': workout_type,
            'duration': duration,  # in minutes
            'calories': calories,
            'notes': notes,
            'timestamp': datetime.now().isoformat()
        }
        self.workout_history.append(workout)
        logger.info(f"Workout logged: {workout_type} - {duration}min, {calories}kcal")
        return workout

    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, Any]:
        """Get daily fitness statistics."""
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')

        today_workouts = [w for w in self.workout_history 
                         if w['timestamp'].startswith(date)]

        total_calories = sum(w['calories'] for w in today_workouts)
        total_duration = sum(w['duration'] for w in today_workouts)
        workout_count = len(today_workouts)

        return {
            'date': date,
            'workouts': workout_count,
            'total_duration': total_duration,
            'total_calories': total_calories,
            'avg_duration': total_duration / workout_count if workout_count > 0 else 0
        }

    def get_advice(self) -> str:
        """Provide AI-powered fitness advice."""
        stats = self.get_daily_stats()
        
        if stats['workouts'] == 0:
            return "💪 You haven't worked out today. Time to get moving!"
        elif stats['workouts'] >= 2:
            return "🔥 Great job! You've had multiple workouts today. Stay hydrated!"
        else:
            return "👍 Good start! You could fit in another quick session today."

    def set_goal(self, goal_type: str, target_value: int, timeframe: str) -> bool:
        """Set a fitness goal."""
        goal = {
            'type': goal_type,
            'target': target_value,
            'timeframe': timeframe,
            'created_at': datetime.now().isoformat()
        }
        self.goals[goal_type] = goal
        logger.info(f"Goal set: {goal_type} - {target_value} {timeframe}")
        return True
