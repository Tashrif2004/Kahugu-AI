import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';

import HomeScreen from './screens/HomeScreen';
import ContentCreatorScreen from './screens/ContentCreatorScreen';
import CommunicationsScreen from './screens/CommunicationsScreen';
import MarketIntelScreen from './screens/MarketIntelScreen';
import SchedulerScreen from './screens/SchedulerScreen';
import DigistoreScreen from './screens/DigistoreScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={({ route }) => ({
            headerShown: false,
            tabBarIcon: ({ focused, color, size }) => {
              let iconName: keyof typeof Ionicons.glyphMap = 'home';
              if (route.name === 'Home') iconName = 'home';
              else if (route.name === 'Content') iconName = 'create';
              else if (route.name === 'Comms') iconName = 'chatbubbles';
              else if (route.name === 'Intel') iconName = 'analytics';
              else if (route.name === 'Schedule') iconName = 'calendar';
              else if (route.name === 'Store') iconName = 'cart';
              return <Ionicons name={iconName} size={size} color={color} />;
            },
            tabBarActiveTintColor: '#00E5FF',
            tabBarInactiveTintColor: '#666',
            tabBarStyle: {
              backgroundColor: '#0A0A0A',
              borderTopColor: '#1A1A2E',
              paddingBottom: 5,
              height: 60,
            },
            tabBarLabelStyle: { fontSize: 10 },
          })}
        >
          <Tab.Screen name="Home" component={HomeScreen} />
          <Tab.Screen name="Content" component={ContentCreatorScreen} options={{ title: 'Content' }} />
          <Tab.Screen name="Comms" component={CommunicationsScreen} options={{ title: 'Comms' }} />
          <Tab.Screen name="Intel" component={MarketIntelScreen} options={{ title: 'Intel' }} />
          <Tab.Screen name="Schedule" component={SchedulerScreen} options={{ title: 'Schedule' }} />
          <Tab.Screen name="Store" component={DigistoreScreen} options={{ title: 'Store' }} />
        </Tab.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
