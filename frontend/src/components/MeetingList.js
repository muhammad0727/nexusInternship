import React, { useState, useEffect } from 'react';

const MeetingList = () => {
  const [meetings, setMeetings] = useState([]);

  useEffect(() => {
    fetch('/api/meetings/')
      .then(response => response.json())
      .then(data => setMeetings(data));
  }, []);

  return (
    <div>
      <h2>Meetings</h2>
      <ul>
        {meetings.map(meeting => (
          <li key={meeting.id}>{meeting.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default MeetingList;