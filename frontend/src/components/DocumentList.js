import React, { useState, useEffect } from 'react';

const DocumentList = () => {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    fetch('/api/documents/')
      .then(response => response.json())
      .then(data => setDocuments(data));
  }, []);

  return (
    <div>
      <h2>Documents</h2>
      <ul>
        {documents.map(document => (
          <li key={document.id}>{document.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default DocumentList;