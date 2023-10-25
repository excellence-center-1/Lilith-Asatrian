import React, { useEffect, useState } from "react";

const Contacts = () => {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newContact, setNewContact] = useState({
    name: "",
    surname: "",
    phone_number: "",
    work_place: "",
  });
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewContact((prevContact) => ({
      ...prevContact,
      [name]: value,
    }));
  };
  const handleContact = async () => {
    try {
      const userId = localStorage.getItem("userId");
      const response = await fetch(
        `http://localhost:5000/contacts/add?userId=${userId}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newContact),
        }
      );
      if (response.ok) {
        console.log("Contact added successfully");
        setContacts((prevContact) => [...prevContact, newContact]);
      } else {
        console.log("Error occurred posting contact");
      }
    } catch (error) {
      console.log("Error:", error);
    }
  };
  const handleOpen = () => {
    setIsModalOpen(true);
  };
  const handleClose = () => {
    setIsModalOpen(false);
  };
  const fetchContacts = async () => {
    try {
      const userId = localStorage.getItem("userId");
      const response = await fetch(
        `http://localhost:5000/contacts?userId=${userId}`
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      if (Array.isArray(data)) {
        setContacts(data);
      } else {
        console.error("Data is not an array:", data);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchContacts();
  }, []);

  return (
    <div>
      <h1>Contacts</h1>
      <button onClick={handleOpen}>Add Contact</button>
      {isModalOpen && (
        <div>
          <div>
            <span onClick={handleClose}>&times;</span>
            <h2>Create Contact</h2>
            <form>
              <label htmlFor="name">Name:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={newContact.name}
                onChange={handleInputChange}
              />
              <label htmlFor="surname">Surname:</label>
              <input
                type="text"
                id="surname"
                name="surname"
                value={newContact.surname}
                onChange={handleInputChange}
              />
              <label htmlFor="phone_number">Phone Number:</label>
              <input
                type="text"
                id="phone_number"
                name="phone_number"
                value={newContact.phone_number}
                onChange={handleInputChange}
              />
              <label htmlFor="work_place">Work place:</label>
              <input
                type="text"
                id="work_place"
                name="work_place"
                value={newContact.work_place}
                onChange={handleInputChange}
              />
              <button type="button" onClick={handleContact}>
                Save
              </button>
            </form>
          </div>
        </div>
      )}
      <table style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid black", padding: "8px" }}>Name</th>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Surname
            </th>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Work Place
            </th>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Phone Number
            </th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact, index) => (
            <tr key={index}>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {contact.name}
              </td>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {contact.surname}
              </td>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {contact.work_place}
              </td>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {contact.phone_number}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Contacts;
