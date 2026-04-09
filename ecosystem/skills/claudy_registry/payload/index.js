const axios = require('axios');
const { getFirestore, collection, addDoc } = require('firebase-admin/firestore');

// Initialize Firestore
const db = getFirestore();

async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    const data = response.data;
    
    // Write to Firestore
    const docRef = await addDoc(collection(db, 'data'), { ...data });
    console.log(`Document written with ID: ${docRef.id}`);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Schedule the function to run every hour
setInterval(fetchData, 3600000);