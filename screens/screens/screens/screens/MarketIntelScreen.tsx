import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, ActivityIndicator } from 'react-native';
import { askJarvis } from '../services/openai';

export default function MarketIntelScreen({ route }: any) {
  const tool = route.params?.tool || 'trend';
  const [data, setData] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const prompts: any = {
    trend: 'Changanua hii data ya mitandao ya kijamii na upendekeze trend na muda bora wa kuposti: ',
    competitor: 'Linganisha wasifu huu wa mshindani na wetu, toa mapendekezo ya maudhui: ',
  };

  const analyze = async () => {
    if (!data.trim()) return;
    setLoading(true);
    const analysis = await askJarvis(prompts[tool] + data);
    setResult(analysis);
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        {tool === 'trend' ? 'Trend Analyzer' : 'Competitor Analysis'}
      </Text>
      <TextInput
        style={styles.input}
        placeholder="Bandika data ya post, metrics au wasifu..."
        placeholderTextColor="#555"
        value={data}
        onChangeText={setData}
        multiline
      />
      <TouchableOpacity style={styles.button} onPress={analyze} disabled={loading}>
        <Text style={styles.buttonText}>{loading ? 'Inachambua...' : 'Chambua'}</Text>
      </TouchableOpacity>
      {result ? (
        <ScrollView style={styles.analysisBox}>
          <Text style={styles.analysisText}>{result}</Text>
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
  analysisBox: { backgroundColor: '#111', padding: 15, borderRadius: 12, flex: 1 },
  analysisText: { color: '#DDD', lineHeight: 22 },
});
