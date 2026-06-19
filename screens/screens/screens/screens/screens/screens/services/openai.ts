const OPENAI_API_KEY = 'sk-your-actual-key-here';

const API_URL = 'https://api.openai.com/v1/chat/completions';

export async function askJarvis(prompt: string): Promise<string> {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.7,
      }),
    });
    const data = await response.json();
    return data.choices[0]?.message?.content || 'No response';
  } catch (error) {
    return 'Error connecting to Jarvis.';
  }
}
