import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import { askJarvis } from '../services/openai';
import { speak } from '../utils/speech';

export default function ContentCreatorScreen({ route }: any) {
  const tool = route.params?.tool || 'pin';
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const prompts: any = {
    pin: 'Andaa caption ya Pinterest yenye keywords na hashtags kuhusu: ',
    ad: 'Andika ad copy ya Facebook/Instagram yenye headline na call-to-action kuhusu: ',
    script: 'Andika script ya video fupi ya Reels/TikTok (dakika 1) kuhusu: ',
    proposal: 'Andika proposal template ya Upwork/Fiverr kwa mteja anahitaji: ',
  };

  const generate = async () => {
    if (!input.trim()) return;
    setLoading(true);
    const result = await askJarvis(prompts[tool] + input);
    setOutput(result);
    setLoading(false);
    speak(result);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        {tool === 'pin' && 'Pin Creator'}
        {tool === 'ad' && 'Ad Copy Generator'}
        {tool === 'script' && 'Video Script Writer'}
        {tool === 'proposal' && 'Proposal Writer'}
      </Text>
      <TextInput
        style={styles.input}
        placeholder="Eleza unachotaka..."
        placeholderTextColor="#555"
        value={input}
        onChangeText={setInput}
        multiline
      />
      <TouchableOpacity style={styles.button} onPress={generate} disabled={loading}>
        <Text style={styles.buttonText}>{loading ? 'Inafanya...' : 'Tengeneza'}</Text>
      </TouchableOpacity>
      {output ? (
        <ScrollView style={styles.outputBox}>
          <Text style={styles.outputText}>{output}</Text>
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
  outputBox: { backgroundColor: '#111', padding: 15, borderRadius: 12, flex: 1 },
  outputText: { color: '#DDD', lineHeight: 22 },
});
