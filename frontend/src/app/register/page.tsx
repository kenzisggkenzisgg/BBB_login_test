"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Register() {
  const [userId, setUserId] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: userId, email, password }), 
    });

    const data = await res.json();

    if (res.ok) {
      alert("登録成功！");
      router.push("/login"); // 登録後はログインページへ
    } else {
      alert(`登録失敗: ${data.detail}`);
    }
  };

  return (
    <div>
      <h2>ユーザー登録</h2>
      <form onSubmit={handleSubmit}>
        <label>ユーザーID:</label>
        <input
          type="text"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />

        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label>パスワード:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">登録</button>
      </form>
    </div>
  );
}

