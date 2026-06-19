import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, Alert } from 'react-native';
import { askJarvis } from '../services/openai';
import * as Speech from 'expo-speech';

export default function SchedulerScreen() {
  const [topic, setTopic] = useState('');
  const [preparedPost, setPreparedPost] = useState('');
  const [loading, setLoading] = useState(false);

  const preparePost = async () => {
    if (!topic.trim()) return;
    setLoading(true);
    const post = await askJarvis(
      `Andaa post kamili ya Instagram/Facebook kuhusu: ${topic}. Jumlisha na caption, hashtags, na image idea.`
    );
    setPreparedPost(post);
    setLoading(false);
    Speech.speak('Post imeandaliwa, bonyeza kutuma', { language: 'sw' });
  };

  const oneTapSend = () => {
    Alert.alert('Imefanikiwa', 'Post imetumwa! (simulation)');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Post Scheduler</Text>
      <TextInput
        style={styles.input}
        placeholder="Mada ya post leo..."
        placeholderTextColor="#555"
        value={topic}
        onChangeText={setTopic}
      />
      <TouchableOpacity style={styles.button} onPress={preparePost} disabled={loading}>
        <Text style={styles.buttonText}>{loading ? 'Inaandaa...' : 'Andaa Post'}</Text>
      </TouchableOpacity>
      {preparedPost ? (
        <ScrollView style={styles.preview}>
          <Text style={styles.previewText}>{preparedPost}</Text>
          <TouchableOpacity style={styles.sendButton} onPress={oneTapSend}>
            <Text style={styles.sendButtonText}>Tuma Kwa Tap Moja</Text>
          </TouchableOpacity>
        </ScrollView>
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0A0A0A', padding: 20, paddingTop: 60 },
  title: { color: '#00E5FF', fontSize: 24, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  input: {
    backgroundColor: '#1A1A2E', color: '#FFF', borderRadius: 12, padding: 15,
    marginBottom: 15, borderColor: '#2A2A3E', borderWidth: 1,
  },
  button: { backgroundColor: '#00E5FF', padding: 15, borderRadius: 12, alignItems: 'center', marginBottom: 20 },
  buttonText: { color: '#000', fontWeight: 'bold' },
  preview: { backgroundColor: '#111', borderRadius: 12, padding: 15, flex: 1 },
  previewText: { color: '#DDD', lineHeight: 22, marginBottom: 20 },
  sendButton: { backgroundColor: '#4CAF50', padding: 15, borderRadius: 12, alignItems: 'center' },
  sendButtonText: { color: '#FFF', fontWeight: 'bold' },
});
