"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function RegisterPage() {

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const registerUser = async () => {
    setLoading(true);
    try {

      const response = await api.post(
        "/auth/register",
        {
          name,
          email,
          password,
        }
      );

      setMessage(response.data.message);

    } catch (error: any) {

      setMessage(
        error.response?.data?.detail ||
        "Registration failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-10 flex flex-col gap-4 max-w-md">

      <h1 className="text-2xl font-bold">
        Register
      </h1>

      <input
        className="
          border
          border-gray-300
          rounded-lg
          p-3
          focus:outline-none
          focus:ring-2
          focus:ring-blue-500
        "
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        className="border p-2"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        className="border p-2"
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={registerUser}
        disabled={loading}
        className="
          border
          border-blue-600
          bg-blue-600
          text-white
          px-4
          py-2
          rounded-lg
          hover:bg-blue-700
          transition
          duration-200
          disabled:bg-gray-400
          disabled:border-gray-400
          disabled:cursor-not-allowed
        "
      >
        {loading ? "Registering..." : "Register"}
      </button>

      <p>{message}</p>

    </div>
  );
}