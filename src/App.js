import React, { useState } from 'react';

function App() {
  const [data, setData] = useState('');
  const [name, setName] = useState(''); // Input for the user's name

  const fetchData = async () => {
    try {
      const response = await fetch(`/api/http_trigger?name=${encodeURIComponent(name)}`);
      if (response.ok) {
        const { text } = await response.json(); // Assumes your function returns JSON with a `text` key
        setData(text);
      } else {
        const errorText = await response.text();
        setData(`Error: ${errorText}`);
      }
    } catch (error) {
      setData(`Error: ${error.message}`);
    }
  };

  return (
    <div>
      <h1>Azure Function Response</h1>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={fetchData}>Fetch Data</button>
      <div>{data}</div>
    </div>
  );
}

export default App;
