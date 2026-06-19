"""Updated Fitness Agent with Enhanced Tracking Service"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
from services.fitness_tracking_service import FitnessTracker

logger = logging.getLogger(__name__)


class FitnessAgent:
    """Tracks workouts, movements, and provides fitness advice."""

    def __init__(self):
        self.name = "Fitness Agent"
        self.tracker = FitnessTracker()
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process fitness command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def log_workout(self, workout_type: str, duration: int, intensity: str = "moderate",
                   calories: Optional[int] = None, distance: Optional[float] = None,
                   location: Optional[str] = None, heart_rate_avg: Optional[int] = None,
                   notes: Optional[str] = None) -> Dict[str, Any]:
        """Log a comprehensive workout session."""
        return self.tracker.log_workout(
            workout_type=workout_type,
            duration=duration,
            intensity=intensity,
            calories=calories,
            distance=distance,
            location=location,
            heart_rate_avg=heart_rate_avg,
            notes=notes
        )

    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, Any]:
        """Get daily fitness statistics."""
        return self.tracker.get_daily_stats(date)

    def get_weekly_stats(self) -> Dict[str, Any]:
        """Get weekly fitness statistics."""
        return self.tracker.get_weekly_stats()

    def get_monthly_stats(self) -> Dict[str, Any]:
        """Get monthly fitness statistics."""
        return self.tracker.get_monthly_stats()

    def set_goal(self, goal_type: str, target_value: int, timeframe: str, unit: str = "") -> Dict[str, Any]:
        """Set a fitness goal."""
        return self.tracker.set_goal(goal_type, target_value, timeframe, unit)

    def get_goals(self) -> Dict[str, Any]:
        """Get all current goals."""
        return self.tracker.get_goals()

    def get_goal_progress(self, goal_type: str) -> Dict[str, Any]:
        """Get progress for a specific goal."""
        return self.tracker.get_goal_progress(goal_type)

    def get_achievements(self) -> list:
        """Get all achievements."""
        return self.tracker.get_achievements()

    def get_advice(self) -> str:
        """Get AI-powered fitness advice."""
        return self.tracker.get_ai_advice()

    def get_all_workouts(self, limit: Optional[int] = None) -> list:
        """Get all logged workouts."""
        if limit:
            return self.tracker.workouts[-limit:]
        return self.tracker.workouts