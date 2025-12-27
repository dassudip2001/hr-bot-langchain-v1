"use client";

import axios from "axios";
import { useState, useRef, useEffect } from "react";
import { SubmitHandler, useForm } from "react-hook-form";

interface Message {
  answer: string;
  status: string;
  sender: "user" | "assistant";
}

interface ChatRequest {
  question: string;
}

export default function HomePage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      answer: "Hello! I'm your AI assistant. How can I help you today?",
      status: "success",
      sender: "assistant",
    },
  ]);

  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const {
    register,
    handleSubmit,
    watch,
    reset,
    formState: { errors },
  } = useForm<ChatRequest>();
  const onSubmit: SubmitHandler<ChatRequest> = (data) => {
    sendMessage(data.question);
    reset();
  };

  const sendMessage = async (question: string) => {
    // Add user message to the chat
    const userMessage: Message = {
      answer: question,
      status: "success",
      sender: "user",
    };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:5003/api/v1/ask", {
        question,
      });
      const assistantMessage: Message = {
        answer:
          response.data.answer ||
          response.data.message ||
          "No response received",
        status: response.data.status || "success",
        sender: "assistant",
      };
      setMessages((prev) => [...prev, assistantMessage]);
      setIsLoading(false);
    } catch (error) {
      console.error("Error sending message:", error);
      const errorMessage: Message = {
        answer: "Sorry, I encountered an error. Please try again.",
        status: "error",
        sender: "assistant",
      };
      setMessages((prev) => [...prev, errorMessage]);
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey && !isLoading) {
      e.preventDefault();
      handleSubmit(onSubmit)();
    }
  };

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [watch("question")]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  return (
    <div className="flex flex-col h-screen bg-white dark:bg-gray-900">
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-3xl mx-auto px-4 py-8">
          {messages.length === 1 && (
            <div className="flex flex-col items-center justify-center h-full text-center py-12">
              <div className="mb-6">
                <div className="w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white text-2xl font-semibold mb-4">
                  AI
                </div>
              </div>
              <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mb-2">
                How can I help you today?
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                Ask me anything or start a conversation
              </p>
            </div>
          )}

          <div className="space-y-6">
            {messages?.map((message, index) => (
              <div
                key={index}
                className={`flex gap-4 ${
                  message.sender === "user" ? "justify-end" : "justify-start"
                }`}
              >
                {message.sender === "assistant" && (
                  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0 mt-1">
                    AI
                  </div>
                )}
                <div
                  className={`max-w-[85%] ${
                    message.sender === "user"
                      ? "bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100"
                      : "text-gray-900 dark:text-gray-100"
                  } rounded-lg px-4 py-3`}
                >
                  <div className="whitespace-pre-wrap break-words leading-relaxed">
                    {message.answer}
                  </div>
                </div>
                {message.sender === "user" && (
                  <div className="w-8 h-8 rounded-full bg-gray-300 dark:bg-gray-700 flex items-center justify-center text-gray-700 dark:text-gray-300 text-sm font-semibold flex-shrink-0 mt-1">
                    U
                  </div>
                )}
              </div>
            ))}

            {isLoading && (
              <div className="flex gap-4 justify-start">
                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0 mt-1">
                  AI
                </div>
                <div className="bg-gray-100 dark:bg-gray-800 rounded-lg px-4 py-3">
                  <div className="flex gap-1">
                    <div
                      className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                      style={{ animationDelay: "0ms" }}
                    ></div>
                    <div
                      className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                      style={{ animationDelay: "150ms" }}
                    ></div>
                    <div
                      className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                      style={{ animationDelay: "300ms" }}
                    ></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        </div>
      </div>

      {/* Input Area */}
      <div className="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900">
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="max-w-3xl mx-auto px-4 py-4">
            <div className="relative flex items-end gap-2">
              <div className="flex-1 relative">
                <textarea
                  {...register("question")}
                  onKeyPress={handleKeyPress}
                  placeholder="Message..."
                  rows={1}
                  disabled={isLoading}
                  className="w-full px-4 py-3 pr-12 bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-2xl text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none overflow-hidden max-h-32"
                />
              </div>
              <button
                type="submit"
                disabled={isLoading}
                className="p-3 bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 dark:disabled:bg-gray-700 disabled:cursor-not-allowed text-white rounded-full transition-colors flex-shrink-0 flex items-center justify-center"
              >
                {!isLoading ? (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="lucide lucide-send-horizontal-icon lucide-send-horizontal"
                  >
                    <path d="M3.714 3.048a.498.498 0 0 0-.683.627l2.843 7.627a2 2 0 0 1 0 1.396l-2.842 7.627a.498.498 0 0 0 .682.627l18-8.5a.5.5 0 0 0 0-.904z" />
                    <path d="M6 12h16" />
                  </svg>
                ) : (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="animate-spin"
                  >
                    <path d="M21 12a9 9 0 1 1-6.219-8.56" />
                  </svg>
                )}
              </button>
            </div>
            <p className="text-xs text-gray-500 dark:text-gray-400 text-center mt-2">
              AI can make mistakes. Check important info.
            </p>
          </div>
        </form>
      </div>
    </div>
  );
}
