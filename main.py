#!/usr/bin/env python3
"""CAUGU - Central Agent AI with User Generation

Main entry point for the CAUGU system.
"""

import logging
from agents.central_agent import CentralAgent
from utils.config import Config
from utils.logger import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


def main():
    """Main function to start CAUGU system."""
    try:
        # Initialize central agent
        caugu = CentralAgent()
        caugu.initialize()

        # Enable default agents
        for agent in ['communication', 'knowledge', 'fitness', 'social_media', 'creative', 'info']:
            caugu.enable_agent(agent)

        # Start the system
        caugu.start()

        # Interactive command loop
        print("\n💬 Type 'help' for commands, 'quit' to exit\n")
        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                if user_input.lower() == 'quit':
                    print("\n👋 CAUGU shutting down... Goodbye!")
                    break

                if user_input.lower() == 'help':
                    print_help()
                    continue

                if user_input.lower() == 'status':
                    import json
                    print(json.dumps(caugu.get_status(), indent=2))
                    continue

                # Process user command
                response = caugu.process_command(
                    user_id='user_001',
                    command=user_input
                )

                print(f"\nCAUGU: {response.get('status')}")
                if 'results' in response:
                    for agent, result in response['results'].items():
                        print(f"  [{agent}] {result.get('status')}")
                print()

            except KeyboardInterrupt:
                print("\n\n👋 CAUGU shutting down... Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error processing command: {e}")
                print(f"❌ Error: {e}\n")

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal error: {e}")
        raise


def print_help():
    """Print help information."""
    help_text = """
    ✨ CAUGU Commands:
    
    Fitness Commands:
    - "Log a 30 minute workout"
    - "Show me my stats today"
    - "Give me fitness advice"
    
    Social Media Commands:
    - "Post on twitter: My message"
    - "Show pending posts"
    
    Creative Commands:
    - "Generate an image of a sunset"
    - "Create electronic music"
    
    Information Commands:
    - "Find gyms near me"
    - "What's the weather?"
    - "Search for AI tutorials"
    
    System Commands:
    - "status" - Show system status
    - "help" - Show this help
    - "quit" - Exit CAUGU
    """
    print(help_text)


if __name__ == '__main__':
    main()
