import React, { useState } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator,
} from 'react-native';
import { askJarvis } from '../services/openai';

export default function ChatScreen() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);
    try {
      const reply = await askJarvis(input);
      const jarvisMsg = { role: 'assistant', content: reply };
      setMessages(prev => [...prev, jarvisMsg]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'system', content: 'Hitilafu imetokea.' }]);
    }
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>💬 Jarvis Chat</Text>
      <ScrollView style={styles.chatArea} contentContainerStyle={{ padding: 10 }}>
        {messages.map((msg, i) => (
          <View
            key={i}
            style={[
              styles.bubble,
              msg.role === 'user' ? styles.userBubble : styles.jarvisBubble,
            ]}
          >
            <Text style={msg.role === 'user' ? styles.userText : styles.jarvisText}>
              {msg.content}
            </Text>
          </View>
        ))}
        {loading && <ActivityIndicator color="#00E5FF" style={{ margin: 10 }} />}
      </ScrollView>
      <View style={styles.inputRow}>
        <TextInput
          style={styles.input}
          placeholder="Andika ujumbe..."
          placeholderTextColor="#555"
          value={input}
          onChangeText={setInput}
          multiline
        />
        <TouchableOpacity style={styles.sendBtn} onPress={sendMessage} disabled={loading}>
          <Ionicons name="send" size={24} color="#000" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

import { Ionicons } from '@expo/vector-icons';

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0A0A0A', paddingTop: 50 },
  header: { color: '#00E5FF', fontSize: 22, fontWeight: 'bold', textAlign: 'center', marginBottom: 10 },
  chatArea: { flex: 1, marginHorizontal: 10 },
  bubble: {
    maxWidth: '80%', padding: 12, borderRadius: 16, marginVertical: 4,
  },
  userBubble: { alignSelf: 'flex-end', backgroundColor: '#00E5FF' },
  jarvisBubble: { alignSelf: 'flex-start', backgroundColor: '#1A1A2E' },
  userText: { color: '#000' },
  jarvisText: { color: '#DDD' },
  inputRow: { flexDirection: 'row', padding: 10, alignItems: 'flex-end', borderTopColor: '#2A2A3E', borderTopWidth: 1 },
  input: {
    flex: 1, backgroundColor: '#1A1A2E', color: '#FFF', borderRadius: 20, paddingHorizontal: 15,
    paddingVertical: 10, maxHeight: 100,
  },
  sendBtn: {
    backgroundColor: '#00E5FF', borderRadius: 25, width: 50, height: 50, justifyContent: 'center', alignItems: 'center', marginLeft: 10,
  },
});
