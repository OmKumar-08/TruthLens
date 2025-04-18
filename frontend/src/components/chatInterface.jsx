import React, { useState } from 'react';
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
} from '@chatscope/chat-ui-kit-react';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { sendMessage } from '../api';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = async (innerHtml) => {
    const userMessage = {
      direction: 'outgoing',
      message: innerHtml,
      sender: 'User',
    };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      const response = await sendMessage(innerHtml);
      const botMessage = {
        direction: 'incoming',
        message: response.data.report,
        sender: 'Misinfo Guard AI',
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = {
        direction: 'incoming',
        message: 'An error occurred. Please try again.',
        sender: 'Misinfo Guard AI',
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div style={{ position: 'relative', height: '500px' }}>
      <MainContainer>
        <ChatContainer>
          <MessageList>
            {messages.map((msg, i) => (
              <Message key={i} model={msg} />
            ))}
          </MessageList>
          <MessageInput placeholder="Type your message here" onSend={handleSend} />
        </ChatContainer>
      </MainContainer>
    </div>
  );
};

export default ChatInterface;
