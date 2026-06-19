"""Central Agent - Main Orchestrator for CAUGU"""

import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
import json

logger = logging.getLogger(__name__)


class CentralAgent:
    """Main orchestrator that coordinates all sub-agents."""

    def __init__(self):
        self.name = "CAUGU"
        self.version = "1.0.0"
        self.agents = {}
        self.active_agents = set()
        self.command_history = []
        self.context = {}
        self.approval_queue = []
        logger.info(f"Initializing {self.name} Central Agent v{self.version}")

    def initialize(self):
        """Initialize all sub-agents."""
        try:
            logger.info("Initializing all sub-agents...")
            # Import and initialize agents
            from agents.communication_agent import CommunicationAgent
            from agents.social_media_agent import SocialMediaAgent
            from agents.fitness_agent import FitnessAgent
            from agents.knowledge_agent import KnowledgeAgent
            from agents.creative_agent import CreativeAgent
            from agents.info_agent import InfoAgent

            self.agents = {
                'communication': CommunicationAgent(),
                'social_media': SocialMediaAgent(),
                'fitness': FitnessAgent(),
                'knowledge': KnowledgeAgent(),
                'creative': CreativeAgent(),
                'info': InfoAgent(),
            }
            logger.info(f"Initialized {len(self.agents)} agents")
        except Exception as e:
            logger.error(f"Error initializing agents: {e}")
            raise

    def enable_agent(self, agent_name: str) -> bool:
        """Enable a specific agent."""
        if agent_name in self.agents:
            self.active_agents.add(agent_name)
            logger.info(f"Enabled agent: {agent_name}")
            return True
        logger.warning(f"Agent not found: {agent_name}")
        return False

    def disable_agent(self, agent_name: str) -> bool:
        """Disable a specific agent."""
        if agent_name in self.active_agents:
            self.active_agents.remove(agent_name)
            logger.info(f"Disabled agent: {agent_name}")
            return True
        return False

    def process_command(self, user_id: str, command: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Process a user command and route to appropriate agents."""
        try:
            logger.info(f"Processing command from {user_id}: {command}")

            # Store command in history
            self.command_history.append({
                'user_id': user_id,
                'command': command,
                'context': context,
                'timestamp': datetime.now().isoformat()
            })

            # Analyze command to determine which agent(s) to use
            agent_routes = self._route_command(command, context)

            results = {}
            for agent_name in agent_routes:
                if agent_name in self.active_agents:
                    agent = self.agents.get(agent_name)
                    if agent:
                        result = agent.process(command)
                        results[agent_name] = result

            return {
                'status': 'success',
                'command': command,
                'results': results,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error processing command: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def request_approval(self, request_data: Dict[str, Any]) -> bool:
        """Request user approval for an action (e.g., social media post)."""
        approval_request = {
            'id': len(self.approval_queue),
            'data': request_data,
            'timestamp': datetime.now().isoformat(),
            'status': 'pending'
        }
        self.approval_queue.append(approval_request)
        logger.info(f"Approval request created: {approval_request['id']}")

        # In real implementation, this would notify user via Telegram/UI
        print(f"\n🔔 APPROVAL REQUEST #{approval_request['id']}")
        print(f"Type: {request_data.get('type')}")
        print(f"Content: {request_data.get('content')}")
        print("Awaiting user approval...")

        # Placeholder: return True for now
        return True

    def _route_command(self, command: str, context: Optional[str] = None) -> List[str]:
        """Determine which agents should handle this command."""
        routes = []
        cmd_lower = command.lower()

        # Keyword-based routing
        if any(word in cmd_lower for word in ['workout', 'fitness', 'exercise', 'steps', 'calories']):
            routes.append('fitness')

        if any(word in cmd_lower for word in ['post', 'social', 'tweet', 'instagram', 'facebook']):
            routes.append('social_media')

        if any(word in cmd_lower for word in ['music', 'generate', 'create', 'image', 'picture', 'photo']):
            routes.append('creative')

        if any(word in cmd_lower for word in ['notify', 'alert', 'remind', 'message']):
            routes.append('communication')

        if any(word in cmd_lower for word in ['map', 'location', 'nearby', 'weather', 'search']):
            routes.append('info')

        # Default to knowledge agent for questions
        if not routes or any(word in cmd_lower for word in ['what', 'how', 'why', 'explain', 'tell']):
            routes.append('knowledge')

        return list(set(routes))  # Remove duplicates

    def get_status(self) -> Dict[str, Any]:
        """Get current system status."""
        return {
            'name': self.name,
            'version': self.version,
            'active_agents': list(self.active_agents),
            'total_agents': len(self.agents),
            'commands_processed': len(self.command_history),
            'pending_approvals': len([a for a in self.approval_queue if a['status'] == 'pending']),
            'timestamp': datetime.now().isoformat()
        }

    def start(self):
        """Start CAUGU system."""
        logger.info(f"🚀 Starting {self.name} system...")
        print(f"\n{'='*50}")
        print(f"  {self.name} - AI Assistant System")
        print(f"  Version {self.version}")
        print(f"  Status: {self.get_status()}")
        print(f"{'='*50}\n")
