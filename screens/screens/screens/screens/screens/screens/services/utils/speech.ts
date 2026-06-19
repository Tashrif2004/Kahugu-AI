import * as Speech from 'expo-speech';

export function speak(text: string) {
  Speech.speak(text, {
    language: 'sw',
    pitch: 1.0,
    rate: 0.9,
  });
}
