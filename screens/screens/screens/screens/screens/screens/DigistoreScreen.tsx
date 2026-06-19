import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import { askJarvis } from '../services/openai';

export default function DigistoreScreen() {
  const [keyword, setKeyword] = useState('');
  const [results, setResults] = useState('');
  const [loading, setLoading] = useState(false);

  const searchProducts = async () => {
    if (!keyword.trim()) return;
    setLoading(true);
    const prompt = `You are a Digistore24 product expert. Based on the keyword "${keyword}", 
    suggest 3-5 trending, winning products with high commissions available on Digistore24. 
    For each product provide: Product Name, Commission Rate, Why it's winning/trending. 
    Keep the answer concise and in a list. Language: Swahili or English mixed as appropriate.`;
    const result = await askJarvis(prompt);
    setResults(result);
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Digistore24 Finder</Text>
      <Text style={styles.subtitle}>Tafuta bidhaa zenye mauzo makubwa na commission kubwa</Text>
      <TextInput
        style={styles.input}
        placeholder="Mfano: afya, utajiri, mazoezi, online business..."
        placeholderTextColor="#555"
        value={keyword}
        onChangeText={setKeyword}
      />
      <TouchableOpacity style={styles.button} onPress={searchProducts} disabled={loading}>
        <Text style={styles.buttonText}>
          {loading ? 'Inatafuta...' : 'Tafuta Bidhaa'}
        </Text>
      </TouchableOpacity>
      {results ? (
        <ScrollView style={styles.resultBox}>
          <Text style={styles.resultText}>{results}</Text>
        </ScrollView>
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0A0A0A', padding: 20, paddingTop: 60 },
  title: { color: '#00E5FF', fontSize: 24, fontWeight: 'bold', textAlign: 'center' },
  subtitle: { color: '#888', fontSize: 14, textAlign: 'center', marginBottom: 20 },
  input: {
    backgroundColor: '#1A1A2E', color: '#FFF', borderRadius: 12, padding: 15,
    marginBottom: 15, borderColor: '#2A2A3E', borderWidth: 1,
  },
  button: { backgroundColor: '#00E5FF', padding: 15, borderRadius: 12, alignItems: 'center', marginBottom: 20 },
  buttonText: { color: '#000', fontWeight: 'bold', fontSize: 16 },
  resultBox: { backgroundColor: '#111', padding: 15, borderRadius: 12, flex: 1 },
  resultText: { color: '#DDD', lineHeight: 22 },
});
