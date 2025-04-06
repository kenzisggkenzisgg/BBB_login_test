"use client";

import { useEffect, useState } from "react";

export default function ProtectedPage() {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProtectedData = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        setError("トークンが見つかりません。ログインしてください。");
        return;
      }

      const res = await fetch("http://localhost:8000/protected", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();

      if (res.ok) {
        setMessage(data.message);
      } else {
        setError(data.detail || "保護ページの取得に失敗しました");
      }
    };

    fetchProtectedData();
  }, []);

  return (
    <div>
      <h2>保護されたページ</h2>
      {message && <p>{message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
