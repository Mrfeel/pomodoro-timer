#!/usr/bin/env python3
"""
Pomodoro Timer — A clean desktop productivity timer.
25 min Work → 5 min Short Break → repeat (15 min Long Break every 4th session)
"""

import tkinter as tk
from tkinter import ttk
import time
import math
import platform
import sys

# --- Constants ---
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
POMODOROS_BEFORE_LONG_BREAK = 4

# Color palette
COLORS = {
    "work":       "#E74C3C",  # Red
    "work_light": "#FADBD8",
    "short_break":       "#27AE60",  # Green
    "short_break_light": "#D5F5E3",
    "long_break":       "#2980B9",  # Blue
    "long_break_light": "#D6EAF8",
    "bg":          "#2C3E50",  # Dark navy
    "bg_light":    "#34495E",
    "text":        "#ECF0F1",
    "text_dim":    "#95A5A6",
    "button_bg":   "#3D566E",
    "button_fg":   "#ECF0F1",
    "button_hover": "#4A6A8A",
    "pause":       "#F39C12",
    "reset":       "#7F8C8D",
}


class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")
        self.root.configure(bg=COLORS["bg"])
        self.root.resizable(False, False)

        # Window size and centering
        self.WIDTH = 420
        self.HEIGHT = 520
        self._center_window()

        # Prevent closing on Esc by mistake — bind quit to Ctrl+Q or window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        # --- State ---
        self.modes = ["work", "short_break", "long_break"]
        self.current_mode = "work"
        self.remaining_seconds = WORK_MINUTES * 60
        self.total_seconds = WORK_MINUTES * 60
        self.is_running = False
        self.is_paused = False
        self.pomodoro_count = 0  # Completed work sessions
        self.always_on_top = tk.BooleanVar(value=False)
        self._after_id = None

        # --- Build UI ---
        self._build_ui()
        self._update_display()

    # ── Window helpers ──────────────────────────────────────────
    def _center_window(self):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - self.WIDTH) // 2
        y = (screen_h - self.HEIGHT) // 2
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

    def _on_close(self):
        if self._after_id is not None:
            self.root.after_cancel(self._after_id)
        self.root.destroy()

    # ── Sound ────────────────────────────────────────────────────
    def _play_sound(self):
        """Cross-platform sound notification."""
        sys_name = platform.system()
        try:
            if sys_name == "Windows":
                import winsound
                # Three beeps to get attention
                for _ in range(3):
                    winsound.Beep(1000, 200)
                    time.sleep(0.1)
            elif sys_name == "Darwin":  # macOS
                import os
                os.system("afplay /System/Library/Sounds/Glass.aiff")
            else:  # Linux
                import os
                os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || "
                          "aplay /usr/share/sounds/alsa/Front_Center.wav 2>/dev/null || true")
        except Exception:
            # Last resort: terminal bell
            print("\a", end="", flush=True)

    # ── UI Construction ──────────────────────────────────────────
    def _build_ui(self):
        # --- Always-on-top toggle (top-right) ---
        top_frame = tk.Frame(self.root, bg=COLORS["bg"])
        top_frame.pack(fill="x", padx=16, pady=(12, 0))

        self.top_cb = tk.Checkbutton(
            top_frame,
            text="📌 置顶窗口",
            variable=self.always_on_top,
            command=self._toggle_always_on_top,
            bg=COLORS["bg"],
            fg=COLORS["text_dim"],
            selectcolor=COLORS["bg_light"],
            activebackground=COLORS["bg"],
            activeforeground=COLORS["text"],
            font=("Microsoft YaHei", 9),
        )
        self.top_cb.pack(side="right")

        # --- Pomodoro counter ---
        self.counter_label = tk.Label(
            self.root,
            text="",
            bg=COLORS["bg"],
            fg=COLORS["text_dim"],
            font=("Microsoft YaHei", 10),
        )
        self.counter_label.pack(pady=(8, 0))

        # --- Session mode indicator ---
        self.mode_label = tk.Label(
            self.root,
            text="",
            bg=COLORS["bg"],
            font=("Microsoft YaHei", 11, "bold"),
        )
        self.mode_label.pack(pady=(4, 12))

        # --- Canvas for circular progress + timer ---
        self.canvas_size = 260
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_size,
            height=self.canvas_size,
            bg=COLORS["bg"],
            highlightthickness=0,
        )
        self.canvas.pack()

        # --- Control buttons ---
        btn_frame = tk.Frame(self.root, bg=COLORS["bg"])
        btn_frame.pack(pady=(16, 10))

        self.start_btn = tk.Button(
            btn_frame,
            text="▶  开始",
            command=self._start,
            bg=COLORS["short_break"],
            fg="white",
            activebackground="#219A52",
            activeforeground="white",
            font=("Microsoft YaHei", 12, "bold"),
            relief="flat",
            padx=24,
            pady=8,
            cursor="hand2",
        )
        self.start_btn.pack(side="left", padx=6)

        self.pause_btn = tk.Button(
            btn_frame,
            text="⏸  暂停",
            command=self._pause,
            bg=COLORS["pause"],
            fg="white",
            activebackground="#D68910",
            activeforeground="white",
            font=("Microsoft YaHei", 12, "bold"),
            relief="flat",
            padx=24,
            pady=8,
            cursor="hand2",
            state="disabled",
        )
        self.pause_btn.pack(side="left", padx=6)

        self.reset_btn = tk.Button(
            btn_frame,
            text="↺  重置",
            command=self._reset,
            bg=COLORS["reset"],
            fg="white",
            activebackground="#6C7A89",
            activeforeground="white",
            font=("Microsoft YaHei", 12, "bold"),
            relief="flat",
            padx=24,
            pady=8,
            cursor="hand2",
        )
        self.reset_btn.pack(side="left", padx=6)

        # --- Keyboard shortcuts hint ---
        hint = tk.Label(
            self.root,
            text="快捷键: Space 开始/暂停  |  R 重置  |  Ctrl+Q 退出",
            bg=COLORS["bg"],
            fg=COLORS["text_dim"],
            font=("Microsoft YaHei", 8),
        )
        hint.pack(pady=(6, 4))

        # Bind keyboard shortcuts
        self.root.bind("<space>", lambda e: self._start() if not self.is_running else self._pause())
        self.root.bind("<r>", lambda e: self._reset())
        self.root.bind("<R>", lambda e: self._reset())
        self.root.bind("<Control-q>", lambda e: self._on_close())

    # ── Canvas Drawing ───────────────────────────────────────────
    def _update_display(self):
        """Redraw the canvas: circular progress ring + timer text."""
        self.canvas.delete("all")

        cx = self.canvas_size // 2
        cy = self.canvas_size // 2
        radius = 100
        ring_width = 12

        # Background ring
        self.canvas.create_oval(
            cx - radius, cy - radius,
            cx + radius, cy + radius,
            outline=COLORS["bg_light"],
            width=ring_width,
        )

        # Progress arc
        progress = 0.0
        if self.total_seconds > 0:
            progress = self.remaining_seconds / self.total_seconds

        color = COLORS.get(self.current_mode, COLORS["work"])

        if progress > 0:
            # tkinter arcs go counter-clockwise from 3-o'clock; we draw from top (12-o'clock)
            extent = -progress * 360  # negative = clockwise
            self.canvas.create_arc(
                cx - radius, cy - radius,
                cx + radius, cy + radius,
                start=90,
                extent=extent,
                outline=color,
                width=ring_width,
                style="arc",
            )

        # Timer text
        mm, ss = divmod(self.remaining_seconds, 60)
        time_str = f"{mm:02d}:{ss:02d}"

        self.canvas.create_text(
            cx, cy - 12,
            text=time_str,
            fill=COLORS["text"],
            font=("Consolas", 42, "bold"),
            tags="timer_text",
        )

        # Sub-text: total duration hint
        total_mm = self.total_seconds // 60
        self.canvas.create_text(
            cx, cy + 30,
            text=f"/ {total_mm}:00",
            fill=COLORS["text_dim"],
            font=("Microsoft YaHei", 11),
        )

        # --- Update mode & counter labels ---
        mode_names = {
            "work":        "🔴 专注工作",
            "short_break": "🟢 短休息",
            "long_break":  "🔵 长休息",
        }
        self.mode_label.config(text=mode_names.get(self.current_mode, ""), fg=color)

        if self.pomodoro_count > 0:
            self.counter_label.config(text=f"🍅 × {self.pomodoro_count}  已完成")
        else:
            self.counter_label.config(text="准备开始你的第一个番茄钟吧！")

        # Update button states
        if self.is_running and not self.is_paused:
            self.start_btn.config(state="disabled", text="▶  开始")
            self.pause_btn.config(state="normal")
        elif self.is_paused:
            self.start_btn.config(state="normal", text="▶  继续")
            self.pause_btn.config(state="disabled", text="⏸  暂停")
        else:
            self.start_btn.config(state="normal", text="▶  开始")
            self.pause_btn.config(state="disabled", text="⏸  暂停")

    # ── Timer Logic ──────────────────────────────────────────────
    def _tick(self):
        """Called every second when the timer is running."""
        if not self.is_running or self.is_paused:
            return

        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self._update_display()

        if self.remaining_seconds <= 0:
            self._timer_finished()
            return

        # Schedule next tick
        self._after_id = self.root.after(1000, self._tick)

    def _timer_finished(self):
        """Called when the countdown reaches 0."""
        self.is_running = False
        self.is_paused = False
        self._after_id = None

        self._update_display()
        self._play_sound()

        # Auto-advance to next mode
        if self.current_mode == "work":
            self.pomodoro_count += 1
            if self.pomodoro_count % POMODOROS_BEFORE_LONG_BREAK == 0:
                self._switch_mode("long_break")
            else:
                self._switch_mode("short_break")
        else:
            # Break finished → back to work
            self._switch_mode("work")

        self._update_display()

        # Flash the window to get attention (Windows)
        try:
            self.root.attributes("-topmost", True)
            self.root.attributes("-topmost", self.always_on_top.get())
        except Exception:
            pass

    def _switch_mode(self, mode):
        """Switch to a new mode and reset timer to its duration."""
        self.current_mode = mode
        self.is_running = False
        self.is_paused = False

        durations = {
            "work":        WORK_MINUTES * 60,
            "short_break": SHORT_BREAK_MINUTES * 60,
            "long_break":  LONG_BREAK_MINUTES * 60,
        }
        self.remaining_seconds = durations[mode]
        self.total_seconds = durations[mode]

    # ── Button Actions ───────────────────────────────────────────
    def _start(self):
        """Start or resume the timer."""
        if self.is_running and not self.is_paused:
            return  # Already running

        self.is_running = True
        self.is_paused = False
        self._update_display()

        # Cancel any pending tick to avoid double-scheduling
        if self._after_id is not None:
            self.root.after_cancel(self._after_id)
        self._after_id = self.root.after(1000, self._tick)

    def _pause(self):
        """Pause the timer."""
        if not self.is_running or self.is_paused:
            return

        self.is_paused = True
        if self._after_id is not None:
            self.root.after_cancel(self._after_id)
            self._after_id = None
        self._update_display()

    def _reset(self):
        """Reset the timer to the beginning of the current mode."""
        was_running = self.is_running

        self.is_running = False
        self.is_paused = False
        if self._after_id is not None:
            self.root.after_cancel(self._after_id)
            self._after_id = None

        durations = {
            "work":        WORK_MINUTES * 60,
            "short_break": SHORT_BREAK_MINUTES * 60,
            "long_break":  LONG_BREAK_MINUTES * 60,
        }
        self.remaining_seconds = durations[self.current_mode]
        self.total_seconds = durations[self.current_mode]
        self._update_display()

    # ── Always on Top ────────────────────────────────────────────
    def _toggle_always_on_top(self):
        self.root.attributes("-topmost", self.always_on_top.get())


# ── Entry Point ─────────────────────────────────────────────────────
def main():
    root = tk.Tk()

    # Set app icon (optional — skip if not available)
    try:
        # Create a simple icon via bitmap to avoid external file dependency
        pass
    except Exception:
        pass

    app = PomodoroApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
