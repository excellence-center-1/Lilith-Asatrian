import React, { useEffect, useState } from 'react';

const Contacts = () => {
  const [contacts, setContacts] = useState([]);

  const fetchContacts = async () => {
    try {
      const userId = localStorage.getItem('userId');
      const response = await fetch(`http://localhost:5000/contacts?userId=${userId}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      if (Array.isArray(data)) {
        setContacts(data);
      } else {
        console.error('Data is not an array:', data);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchContacts();
  }, []);

  return (
    <div>
      <h1>Contacts</h1>
      <table style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th style={{ border: '1px solid black', padding: '8px' }}>Name</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>Surname</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>Work Place</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>Phone Number</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact, index) => (
            <tr key={index}>
              <td style={{ border: '1px solid black', padding: '8px' }}>{contact.name}</td>
              <td style={{ border: '1px solid black', padding: '8px' }}>{contact.surname}</td>
              <td style={{ border: '1px solid black', padding: '8px' }}>{contact.work_place}</td>
              <td style={{ border: '1px solid black', padding: '8px' }}>{contact.phone_number}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Contacts;
