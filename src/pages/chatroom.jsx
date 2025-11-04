import React, { useState, useRef, useEffect } from "react";
import "./chatroom.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

/**
 * Chatroom (Cozy Luxury Lounge)
 * - Two-column layout: members (left) | chat (right)
 * - Avatars auto-generated with pastel colors (random but stable per name)
 * - Local state messages; ready for backend integration
 * - Auto-scroll + simple simulated replies for demo
 */

const initialMembers = [
    { id: "amrita", name: "Amrita" },
    { id: "akanchha", name: "Akanchha" },
    { id: "abhilasha", name: "Abhilasha" },
    { id: "aditya", name: "Aditya" },
    { id: "ayush", name: "Ayush" },
];

const dummyReplies = [
    "Sounds lovely ✨",
    "That works for me!",
    "I'll book the tickets today.",
    "Love that idea — let's do it!",
    "Can we push it by one day?",
    "Perfect, adding to the plan.",
];

export default function Chatroom() {
    const [members] = useState(initialMembers);
    const [messages, setMessages] = useState([
        {
            id: 1,
            userId: "amrita",
            userName: "Amrita",
            text: "Hey everyone — trip thoughts?",
            time: new Date().toISOString(),
            senderType: "other",
        },
        {
            id: 2,
            userId: "akanchha",
            userName: "Akanchha",
            text: "I was thinking beach + city combo 🌊🏙️",
            time: new Date().toISOString(),
            senderType: "other",
        },
    ]);

    // local user (you)
    const localUser = { id: "you", name: "You" };

    const [input, setInput] = useState("");
    const [typing, setTyping] = useState(false);
    const messagesRef = useRef(null);
    const idRef = useRef(100);

    // auto-scroll when messages change
    useEffect(() => {
        const el = messagesRef.current;
        if (el) {
            el.scrollTop = el.scrollHeight + 200;
        }
    }, [messages]);

    // simulate a friendly reply from a random member (demo)
    const simulateReply = () => {
        const randomMember = members[Math.floor(Math.random() * members.length)];
        const replyText = dummyReplies[Math.floor(Math.random() * dummyReplies.length)];
        const newMsg = {
            id: ++idRef.current,
            userId: randomMember.id,
            userName: randomMember.name,
            text: replyText,
            time: new Date().toISOString(),
            senderType: "other",
        };
        setTimeout(() => {
            setMessages((prev) => [...prev, newMsg]);
            setTyping(false);
        }, 900 + Math.random() * 1200);
    };

    const sendMessage = () => {
        const trimmed = input.trim();
        if (!trimmed) return;
        const newMsg = {
            id: ++idRef.current,
            userId: localUser.id,
            userName: localUser.name,
            text: trimmed,
            time: new Date().toISOString(),
            senderType: "user",
        };
        setMessages((prev) => [...prev, newMsg]);
        setInput("");
        setTyping(true);
        simulateReply(); // demo reply
    };

    const handleKey = (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    };

    // stable pastel color per name (hash -> hue)
    function colorForName(name) {
        let h = 0;
        for (let i = 0; i < name.length; i++) {
            h = name.charCodeAt(i) + ((h << 5) - h);
            h = h & h;
        }
        const hue = Math.abs(h) % 360;
        // pastel HSL
        return `hsl(${hue} 50% 70%)`;
    }

    function initials(name) {
        return name
            .split(" ")
            .map((n) => n[0])
            .slice(0, 2)
            .join("")
            .toUpperCase();
    }

    return (
        <div className="chatroom-page">
            <div className="chat-bg" />
            <div className="chat-wrap">
                {/* Members */}
                <aside className="members-panel glass">
                    <div className="members-header">
                        <h3>Members</h3>
                        <div className="members-count">{members.length}</div>
                    </div>
                    <ul className="members-list">
                        {members.map((m) => (
                            <li key={m.id} className="member-item">
                                <div
                                    className="avatar"
                                    style={{ background: colorForName(m.name) }}
                                    title={m.name}
                                >
                                    {initials(m.name)}
                                </div>
                                <div className="member-info">
                                    <div className="member-name">{m.name}</div>
                                    <div className="member-status">online</div>
                                </div>
                            </li>
                        ))}
                    </ul>
                </aside>

                {/* Chat area */}
                <main className="chat-panel glass">
                    <header className="chat-header">
                        <div>
                            <h2>Group Chatroom</h2>
                            <div className="subtle">Trip planning • Cozy lounge</div>
                        </div>
                        <div className="chat-actions">
                            <button className="icon-btn" title="Members">
                                <i className="fa-solid fa-users"></i>
                            </button>
                            <button className="icon-btn" title="Settings">
                                <i className="fa-solid fa-gear"></i>
                            </button>
                        </div>
                    </header>

                    <div ref={messagesRef} className="messages-area">
                        {messages.map((m) => (
                            <MessageBubble
                                key={m.id}
                                msg={m}
                                isMine={m.senderType === "user"}
                                color={m.userId === localUser.id ? colorForName(localUser.name) : colorForName(m.userName)}
                                initials={initials(m.userName)}
                            />
                        ))}

                        {/* typing indicator */}
                        {typing && (
                            <div className="typing-row">
                                <div className="bubble other">
                                    <div className="typing">
                                        <span />
                                        <span />
                                        <span />
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>

                    <div className="composer">
                        <textarea
                            className="message-input"
                            placeholder="Type your message... (Enter to send)"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKey}
                            rows={1}
                        />
                        <button className="send-btn" onClick={sendMessage} title="Send message">
                            <i className="fa-solid fa-paper-plane"></i>
                        </button>
                    </div>
                </main>
            </div>
        </div>
    );
}

/* --- Message bubble component --- */
function MessageBubble({ msg, isMine, color, initials }) {
    const time = new Date(msg.time).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    return (
        <div className={`message-row ${isMine ? "mine" : "theirs"}`}>
            {!isMine && (
                <div className="msg-avatar" style={{ background: color }}>
                    {initials}
                </div>
            )}

            <div className={`bubble ${isMine ? "user" : "other"}`}>
                <div className="bubble-meta">
                    {!isMine && <span className="meta-name">{msg.userName}</span>}
                    <span className="meta-time">{time}</span>
                </div>
                <div className="bubble-text">{msg.text}</div>
            </div>

            {isMine && (
                <div className="msg-avatar" style={{ background: color }}>
                    {initials}
                </div>
            )}
        </div>
    );
}
