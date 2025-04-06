"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Login() {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: userId, password }), // 👈 修正ポイント
    });

    const data = await res.json();

    if (res.ok) {
      localStorage.setItem("token", data.access_token);
      alert("ログイン成功！");
      router.push("/protected");
    } else {
      alert(`ログイン失敗: ${data.detail}`);
    }
  };

  return (
    <div>
      <h2>ログイン</h2>
      <form onSubmit={handleSubmit}>
        <label>ユーザーID:</label>
        <input type="text" value={userId} onChange={(e) => setUserId(e.target.value)} />

        <label>パスワード:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

        <button type="submit">ログイン</button>
      </form>
    </div>
  );
}


