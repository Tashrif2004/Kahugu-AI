import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import { askJarvis } from '../services/openai';

export default function CommunicationsScreen({ route }: any) {
  const tool = route.params?.tool || 'email';
  const [context, setContext] = useState('');
  const [reply, setReply] = useState('');
  const [loading, setLoading] = useState(false);

  const prompts: any = {
    email: 'Chora email ya kujibu kwa ufasaha, ukitumia taarifa hii: ',
    comment: 'Pendekeza jibu la comment hii ya mtandao wa kijamii: ',
  };

  const generate = async () => {
    if (!context.trim()) return;
    setLoading(true);
    const result = await askJarvis(prompts[tool] + context);
    setReply(result);
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        {tool === 'email' ? 'Email Drafter' : 'Comment Responder'}
      </Text>
      <TextInput
        style={styles.input}
        placeholder="Bandika ujumbe uliopokea..."
        placeholderTextColor="#555"
        value={context}
        onChangeText={setContext}
        multiline
      />
      <TouchableOpacity style={styles.button} onPress={generate} disabled={loading}>
        <Text style={styles.buttonText}>{loading ? 'Inawaza...' : 'Chora Jibu'}</Text>
      </TouchableOpacity>
      {reply ? (
        <ScrollView style={styles.replyBox}>
          <Text style={styles.replyText}>{reply}</Text>
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
    minHeight: 100, textAlignVertical: 'top', marginBottom: 15, borderColor: '#2A2A3E', borderWidth: 1,
  },
  button: { backgroundColor: '#00E5FF', padding: 15, borderRadius: 12, alignItems: 'center', marginBottom: 20 },
  buttonText: { color: '#000', fontWeight: 'bold' },
  replyBox: { backgroundColor: '#111', padding: 15, borderRadius: 12, flex: 1 },
  replyText: { color: '#DDD', lineHeight: 22 },
});
