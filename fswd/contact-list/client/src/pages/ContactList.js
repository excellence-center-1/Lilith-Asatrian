//doesn't use db
import React, { useState } from 'react';

function ContactList() {
  const [contacts, setContacts] = useState([]);
  const [newContact, setNewContact] = useState({ name: '', email: '', phone: '' });
  const [idCounter, setIdCounter] = useState(1);
  const [searchTerm, setSearchTerm] = useState('');

  const addContact = () => {
    if (!newContact.name || !newContact.email || !newContact.phone) return;

    const updatedContacts = [...contacts, { ...newContact, id: idCounter }];
    setContacts(updatedContacts);
    setNewContact({ name: '', email: '', phone: '' });
    setIdCounter(idCounter + 1);
  };

  const deleteContact = (contactId) => {
    const updatedContacts = contacts.filter(contact => contact.id !== contactId);
    setContacts(updatedContacts);
  };

  const searchContacts = () => {
    const filteredContacts = contacts.filter(contact => contact.name.toLowerCase().includes(searchTerm.toLowerCase()));
    return filteredContacts;
  };

  return (
    <div>
      <h2>Contact List</h2>
      <div>
        <h3>Add Contact</h3>
        <input
          type="text"
          placeholder="Search by Name"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <input
          type="text"
          value={newContact.name}
          placeholder="Name"
          onChange={(e) => setNewContact({ ...newContact, name: e.target.value })}
        />
        <input
          type="email"
          value={newContact.email}
          placeholder="Email"
          onChange={(e) => setNewContact({ ...newContact, email: e.target.value })}
        />
        <input
          type="tel"
          value={newContact.phone}
          placeholder="Phone"
          onChange={(e) => setNewContact({ ...newContact, phone: e.target.value })}
        />
        <button onClick={addContact}>Add Contact</button>
      </div>
      <div>
        <h3>Contact List</h3>
        {contacts.map(contact => (
          <div key={contact.id}>
            <h4>{contact.name}</h4>
            <p>Email: {contact.email}</p>
            <p>Phone: {contact.phone}</p>
            <button onClick={() => deleteContact(contact.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ContactList;