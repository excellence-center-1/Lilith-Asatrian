import React, { useState, useEffect } from 'react';
import './ContactList.css';

function ContactList() {
  const [contacts, setContacts] = useState([]);
  const [newContact, setNewContact] = useState({ name: '', email: '', phone: '' });
  const [idCounter, setIdCounter] = useState(1);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    try {
      const response = await fetch('http://localhost:4000/contacts');
      const data = await response.json();

      if (response.ok) {
        setContacts(data);
      } else {
        console.log('Error:', data.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const addContact = async () => {
    if (!newContact.name || !newContact.email || !newContact.phone) return;

    const response = await fetch('http://localhost:4000/contacts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newContact),
    });

    if (response.ok) {
      const contact = await response.json();
      const updatedContacts = [...contacts, contact];
      setContacts(updatedContacts);
      setNewContact({ name: '', email: '', phone: '' });
    } else {
      console.log('Error:', response.statusText);
    }
  };

  const deleteContact = async (contactId) => {
    const response = await fetch(`http://localhost:4000/contacts/${contactId}`, {
      method: 'DELETE',
    });

    if (response.ok) {
      const updatedContacts = contacts.filter((contact) => contact.id !== contactId);
      setContacts(updatedContacts);
    } else {
      console.log('Error:', response.statusText);
    }
  };

  const searchContacts = () => {
    const filteredContacts = contacts.filter((contact) =>
      contact.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    return filteredContacts;
  };

  return (
    <div className="contact-list-container">
      <h2>Contact List</h2>
      <div className="add-contact-container">
        <input
          type="text"
          placeholder="Search by Name"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        <input
          type="text"
          value={newContact.name}
          placeholder="Name"
          onChange={(e) => setNewContact({ ...newContact, name: e.target.value })}
          className="add-contact-input"
        />
        <input
          type="email"
          value={newContact.email}
          placeholder="Email"
          onChange={(e) => setNewContact({ ...newContact, email: e.target.value })}
          className="add-contact-input"
        />
        <input
          type="tel"
          value={newContact.phone}
          placeholder="Phone"
          onChange={(e) => setNewContact({ ...newContact, phone: e.target.value })}
          className="add-contact-input"
        />
        <button onClick={addContact} className="add-contact-button">Add Contact</button>
      </div>
      <div className="contact-list">
       
        {searchContacts().map((contact) => (
          <div key={contact.id} className="contact-item">
            <h4>{contact.name}</h4>
            <p>Email: {contact.email}</p>
            <p>Phone: {contact.phone}</p>
            <button onClick={() => deleteContact(contact.id)} className="delete-contact-button">Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ContactList;
