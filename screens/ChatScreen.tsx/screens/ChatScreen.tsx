import React, { useState, useRef } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { askJarvis } from '../services/openai';
import * as Speech from 'expo-speech';

export default function ChatScreen() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const inputRef = useRef<TextInput>(null);

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
      // Soma jibu kwa sauti moja kwa moja
      Speech.speak(reply, { language: 'sw', pitch: 1.0, rate: 0.9 });
    } catch (e) {
      setMessages(prev => [...prev, { role: 'system', content: 'Hitilafu imetokea.' }]);
    }
    setLoading(false);
  };

  const speakMessage = (text: string) => {
    Speech.speak(text, { language: 'sw', pitch: 1.0, rate: 0.9 });
  };

  // Fungua keyboard yenye voice input (hii inafanya kazi kwenye vifaa vingi)
  const focusInputWithVoice = () => {
    inputRef.current?.focus();
    // Kwa bahati nzuri, keyboard ya simu ina kipaza sauti iwapo umeiwezesha.
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>💬 Jarvis Chat</Text>
      <ScrollView
        style={styles.chatArea}
        contentContainerStyle={{ padding: 10 }}
        ref={scrollViewRef => {
          // tumia ref kama unataka kusogeza mwisho
        }}
      >
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
            {/* Ikiwa ni ujumbe wa Jarvis, weka kitufe cha kusoma */}
            {msg.role === 'assistant' && (
              <TouchableOpacity
                style={styles.speakButton}
                onPress={() => speakMessage(msg.content)}
              >
                <Ionicons name="volume-high" size={18} color="#00E5FF" />
              </TouchableOpacity>
            )}
          </View>
        ))}
        {loading && <ActivityIndicator color="#00E5FF" style={{ margin: 10 }} />}
      </ScrollView>
      <View style={styles.inputRow}>
        <TouchableOpacity style={styles.voiceButton} onPress={focusInputWithVoice}>
          <Ionicons name="mic" size={24} color="#00E5FF" />
        </TouchableOpacity>
        <TextInput
          ref={inputRef}
          style={styles.input}
          placeholder="Andika au gusa 🎤 kuzungumza..."
          placeholderTextColor="#555"
          value={input}
          onChangeText={setInput}
          multiline
          returnKeyType="send"
          onSubmitEditing={sendMessage}
          blurOnSubmit={false}
        />
        <TouchableOpacity style={styles.sendBtn} onPress={sendMessage} disabled={loading}>
          <Ionicons name="send" size={24} color="#000" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0A0A0A', paddingTop: 50 },
  header: { color: '#00E5FF', fontSize: 22, fontWeight: 'bold', textAlign: 'center', marginBottom: 10 },
  chatArea: { flex: 1, marginHorizontal: 10 },
  bubble: {
    maxWidth: '80%',
    padding: 12,
    borderRadius: 16,
    marginVertical: 4,
    position: 'relative',
  },
  userBubble: { alignSelf: 'flex-end', backgroundColor: '#00E5FF' },
  jarvisBubble: { alignSelf: 'flex-start', backgroundColor: '#1A1A2E' },
  userText: { color: '#000' },
  jarvisText: { color: '#DDD' },
  speakButton: {
    position: 'absolute',
    right: -8,
    bottom: -8,
    backgroundColor: '#0A0A0A',
    borderRadius: 15,
    width: 30,
    height: 30,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#00E5FF',
  },
  inputRow: {
    flexDirection: 'row',
    padding: 10,
    alignItems: 'flex-end',
    borderTopColor: '#2A2A3E',
    borderTopWidth: 1,
  },
  voiceButton: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#1A1A2E',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 8,
  },
  input: {
    flex: 1,
    backgroundColor: '#1A1A2E',
    color: '#FFF',
    borderRadius: 20,
    paddingHorizontal: 15,
    paddingVertical: 10,
    maxHeight: 100,
  },
  sendBtn: {
    backgroundColor: '#00E5FF',
    borderRadius: 25,
    width: 50,
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 10,
  },
});
