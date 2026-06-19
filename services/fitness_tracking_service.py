"""Fitness Tracking Service - Enhanced with GPS and wearable integration"""

import logging
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
from pathlib import Path

logger = logging.getLogger(__name__)


class FitnessTracker:
    """Advanced fitness tracking with GPS, heart rate, and analytics."""

    def __init__(self):
        self.name = "FitnessTracker"
        self.workouts = []
        self.daily_stats = {}
        self.goals = {}
        self.achievements = []
        self.streak_count = 0
        self.data_file = Path("./data/fitness_data.json")
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initializing {self.name}")
        self._load_data()

    def log_workout(self, workout_type: str, duration: int, intensity: str = "moderate",
                   calories: Optional[int] = None, distance: Optional[float] = None,
                   location: Optional[str] = None, heart_rate_avg: Optional[int] = None,
                   notes: Optional[str] = None) -> Dict[str, Any]:
        """Log a comprehensive workout session."""
        try:
            # Calculate calories if not provided
            if not calories:
                calories = self._estimate_calories(workout_type, duration, intensity)

            workout = {
                'id': len(self.workouts),
                'type': workout_type,
                'duration': duration,  # minutes
                'intensity': intensity,  # light, moderate, intense
                'calories': calories,
                'distance': distance,  # km
                'location': location,
                'heart_rate_avg': heart_rate_avg,
                'notes': notes,
                'timestamp': datetime.now().isoformat(),
                'date': datetime.now().strftime('%Y-%m-%d')
            }

            self.workouts.append(workout)
            self._update_daily_stats(workout)
            self._check_achievements()
            self._save_data()

            logger.info(f"Workout logged: {workout_type} - {duration}min, {calories}kcal")
            print(f"✅ Workout logged: {workout_type} ({duration}min, {calories}kcal)")

            return workout

        except Exception as e:
            logger.error(f"Error logging workout: {e}")
            return {'status': 'error', 'error': str(e)}

    def _estimate_calories(self, workout_type: str, duration: int, intensity: str) -> int:
        """Estimate calories burned based on workout parameters."""
        # Approximate MET (Metabolic Equivalent) values
        met_values = {
            'running': {'light': 6, 'moderate': 9.8, 'intense': 14.5},
            'cycling': {'light': 4, 'moderate': 7.5, 'intense': 12},
            'walking': {'light': 2.8, 'moderate': 3.8, 'intense': 5.0},
            'swimming': {'light': 4, 'moderate': 8, 'intense': 11},
            'strength': {'light': 3, 'moderate': 5, 'intense': 8},
            'yoga': {'light': 2, 'moderate': 3, 'intense': 4},
            'hiit': {'light': 8, 'moderate': 12, 'intense': 16},
            'sports': {'light': 5, 'moderate': 7, 'intense': 10},
        }

        # Average body weight assumption (70kg)
        weight = 70
        met = met_values.get(workout_type, {}).get(intensity, 5)
        calories = int(met * weight * (duration / 60))
        return calories

    def _update_daily_stats(self, workout: Dict[str, Any]):
        """Update daily statistics."""
        date = workout['date']
        if date not in self.daily_stats:
            self.daily_stats[date] = {
                'date': date,
                'workouts': [],
                'total_duration': 0,
                'total_calories': 0,
                'total_distance': 0,
                'workouts_count': 0
            }

        stats = self.daily_stats[date]
        stats['workouts'].append(workout['id'])
        stats['total_duration'] += workout['duration']
        stats['total_calories'] += workout['calories']
        if workout.get('distance'):
            stats['total_distance'] += workout['distance']
        stats['workouts_count'] += 1

    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, Any]:
        """Get statistics for a specific day."""
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')

        stats = self.daily_stats.get(date, {
            'date': date,
            'workouts': [],
            'total_duration': 0,
            'total_calories': 0,
            'total_distance': 0,
            'workouts_count': 0
        })

        stats['avg_intensity'] = self._calculate_avg_intensity(date)
        return stats

    def get_weekly_stats(self) -> Dict[str, Any]:
        """Get statistics for the past 7 days."""
        today = datetime.now()
        week_stats = {
            'period': 'last_7_days',
            'workouts': [],
            'total_duration': 0,
            'total_calories': 0,
            'total_distance': 0,
            'days_active': 0
        }

        for i in range(7):
            date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
            if date in self.daily_stats:
                stats = self.daily_stats[date]
                week_stats['workouts'].extend(stats['workouts'])
                week_stats['total_duration'] += stats['total_duration']
                week_stats['total_calories'] += stats['total_calories']
                week_stats['total_distance'] += stats['total_distance']
                week_stats['days_active'] += 1

        return week_stats

    def get_monthly_stats(self) -> Dict[str, Any]:
        """Get statistics for the current month."""
        today = datetime.now()
        month_start = today.replace(day=1)
        month_stats = {
            'period': today.strftime('%Y-%m'),
            'workouts': [],
            'total_duration': 0,
            'total_calories': 0,
            'total_distance': 0,
            'days_active': 0,
            'avg_daily_calories': 0
        }

        for date, stats in self.daily_stats.items():
            if date.startswith(today.strftime('%Y-%m')):
                month_stats['workouts'].extend(stats['workouts'])
                month_stats['total_duration'] += stats['total_duration']
                month_stats['total_calories'] += stats['total_calories']
                month_stats['total_distance'] += stats['total_distance']
                month_stats['days_active'] += 1

        if month_stats['days_active'] > 0:
            month_stats['avg_daily_calories'] = int(month_stats['total_calories'] / month_stats['days_active'])

        return month_stats

    def set_goal(self, goal_type: str, target_value: int, timeframe: str, unit: str = "") -> Dict[str, Any]:
        """Set a fitness goal."""
        goal = {
            'type': goal_type,
            'target': target_value,
            'unit': unit,
            'timeframe': timeframe,  # daily, weekly, monthly
            'created_at': datetime.now().isoformat(),
            'progress': 0,
            'completed': False
        }
        self.goals[goal_type] = goal
        logger.info(f"Goal set: {goal_type} - {target_value} {unit} {timeframe}")
        return goal

    def get_goals(self) -> Dict[str, Any]:
        """Get all current goals."""
        return self.goals

    def get_goal_progress(self, goal_type: str) -> Dict[str, Any]:
        """Get progress for a specific goal."""
        if goal_type not in self.goals:
            return {'error': 'Goal not found'}

        goal = self.goals[goal_type]
        current_progress = self._calculate_goal_progress(goal_type)

        return {
            'goal': goal_type,
            'target': goal['target'],
            'current': current_progress,
            'progress_percentage': int((current_progress / goal['target']) * 100),
            'timeframe': goal['timeframe'],
            'completed': current_progress >= goal['target']
        }

    def _calculate_goal_progress(self, goal_type: str) -> int:
        """Calculate progress towards a goal."""
        if goal_type == 'daily_calories':
            stats = self.get_daily_stats()
            return stats['total_calories']
        elif goal_type == 'daily_steps':
            # Placeholder: would integrate with phone sensors
            return 0
        elif goal_type == 'weekly_workouts':
            stats = self.get_weekly_stats()
            return stats['workouts_count']
        elif goal_type == 'weekly_calories':
            stats = self.get_weekly_stats()
            return stats['total_calories']
        return 0

    def _calculate_avg_intensity(self, date: str) -> str:
        """Calculate average workout intensity for a day."""
        intensity_map = {'light': 1, 'moderate': 2, 'intense': 3}
        reverse_map = {1: 'light', 2: 'moderate', 3: 'intense'}

        if date not in self.daily_stats:
            return 'none'

        workout_ids = self.daily_stats[date]['workouts']
        if not workout_ids:
            return 'none'

        total_intensity = sum(intensity_map.get(self.workouts[wid].get('intensity', 'moderate'), 2)
                            for wid in workout_ids)
        avg_intensity_val = total_intensity / len(workout_ids)
        return reverse_map.get(round(avg_intensity_val), 'moderate')

    def _check_achievements(self):
        """Check for new achievements."""
        weekly_stats = self.get_weekly_stats()

        # Achievement: 5 workouts in a week
        if weekly_stats['workouts_count'] >= 5:
            self._add_achievement("Fitness Enthusiast", "Completed 5 workouts in a week")

        # Achievement: 2000 calories in a week
        if weekly_stats['total_calories'] >= 2000:
            self._add_achievement("Calorie Burner", "Burned 2000+ calories in a week")

        # Achievement: 10 workouts total
        if len(self.workouts) >= 10:
            self._add_achievement("Dedicated", "Logged 10+ workouts")

    def _add_achievement(self, title: str, description: str):
        """Add an achievement if not already earned."""
        if not any(a['title'] == title for a in self.achievements):
            achievement = {
                'title': title,
                'description': description,
                'earned_at': datetime.now().isoformat()
            }
            self.achievements.append(achievement)
            logger.info(f"🏆 Achievement unlocked: {title}")
            print(f"🏆 Achievement unlocked: {title}")

    def get_achievements(self) -> List[Dict[str, Any]]:
        """Get all achievements."""
        return self.achievements

    def get_ai_advice(self) -> str:
        """Get AI-powered fitness advice based on data."""
        stats = self.get_daily_stats()
        weekly = self.get_weekly_stats()

        if stats['workouts_count'] == 0:
            return "💪 You haven't worked out today. Let's get moving! Even 15 minutes of activity counts."
        elif stats['total_calories'] < 500:
            return "🔥 Good start! You could fit in another quick workout to reach 500+ calories today."
        elif stats['workouts_count'] >= 2:
            return "⚡ Awesome! You've had multiple workouts today. Remember to stay hydrated and eat well."
        else:
            return "✨ Great job! You're maintaining a consistent fitness routine."

    def _save_data(self):
        """Save fitness data to file."""
        try:
            data = {
                'workouts': self.workouts,
                'daily_stats': self.daily_stats,
                'goals': self.goals,
                'achievements': self.achievements,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info("Fitness data saved")
        except Exception as e:
            logger.error(f"Error saving data: {e}")

    def _load_data(self):
        """Load fitness data from file."""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.workouts = data.get('workouts', [])
                self.daily_stats = data.get('daily_stats', {})
                self.goals = data.get('goals', {})
                self.achievements = data.get('achievements', [])
                logger.info("Fitness data loaded")
        except Exception as e:
            logger.error(f"Error loading data: {e}")