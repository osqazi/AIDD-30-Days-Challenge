***Spec-Kit Plus*** is a **methodology framework** for projects development designed to maximize learning and reusability, not just code delivery. It works with your existing AI tools (like Gemini or Claude) to structure your development process, ensuring that the valuable **reasoning** behind decisions is captured alongside the working code.

### Here is a breakdown of Spec-Kit Plus and its core concepts:

---

## 🎯 What is Spec-Kit Plus?

Spec-Kit Plus is an **SDD-RI (Specification-Driven Development with Reusable Intelligence) framework**. In simple terms, it's a structured way to build projects where you focus on clearly defining *what* you're building (the specification) before you start coding, and you actively capture the *intelligence* (the "why" and "how") generated during the process.

The core idea is: **Capture intelligence, not just deliver code.** This intelligence becomes your personal, compounding expertise over time.

---

## ✨ The Two-Output Philosophy

Every feature you build intentionally creates two outputs:

1.  **Working Code (Ephemeral):** This is the final deliverable—the functional feature. It's **temporary** and project-specific; it could be completely rewritten without loss of learned knowledge.
2.  **Reusable Intelligence (Permanent):** This is the documentation of your reasoning, decisions, and successful AI prompt patterns. It's **permanent** and forms your expertise. It's captured in the project's **`history/`** directory through **ADRs** and **PHRs**.

---

## 🧠 Intelligence Architectures

The framework utilizes two complementary types of intelligence to accelerate your work:

### ➡️ Horizontal Intelligence (Your Learning Across Time)

This is the knowledge that flows **from one project to your personal expertise** in the next. The artifacts capture the learning within a project, but the wisdom lives in **you**, making you faster and more confident over time.

* **ADRs (Architectural Decision Records):** Documents the **"WHY"** behind significant decisions, detailing the context, reasons, and trade-offs (e.g., *Why* did we choose PostgreSQL over MongoDB?).
* **PHRs (Prompt History Records):** Logs AI collaboration sessions to capture **"WHAT PROMPTS WORKED"** for a specific task versus which ones failed.

### ⬆️ Vertical Intelligence (Reusable Components)

This is the creation of **active, reusable components** that your AI tool can invoke in future, similar sessions. This builds specialized capabilities for the AI over time.

* **Components:** You create custom **Skills**, **Subagents**, or **Tools/MCP Servers** after a particularly successful session, recognizing that the pattern would work for similar problems.
* **Function:** Unlike PHRs (which are passive records), these components are **active tools** that the agent uses to execute tasks effectively.

---

## 💻 Spec-Kit Plus Core Workflow Phases

The Spec-Kit Plus workflow uses slash commands to structure the AI collaboration. Here are the first five core concepts (workflow phases) you asked to review:

| Workflow Phase | Description | Output/Goal |
| :--- | :--- | :--- |
| **Phase 1: Constitution** | Define the project-wide standards, constraints, and **non-negotiable quality criteria** for success across all work. | Documented project-wide quality standards. |
| **Phase 2: Specification** | Write clear, testable, and unambiguous requirements for the feature using **SMART criteria** (Specific, Measurable, Achievable, Relevant, Time-bound). This is done using the `/sp.specify` slash command. | Clear, executable requirements (in `specs/`). |
| **Phase 4: Planning** | Design the architecture, select technology choices, and determine the *how* of the implementation. Crucially, this phase **documents the rationale** for these choices in **ADRs**. This is done using the `/sp.plan` slash command. | Implementation plans and Architectural Decision Records (ADRs). |
| **Phase 5: Tasks** | Break the planned work down into **atomic, measurable, and independent units**. These are the smallest chunks of work that can be executed and validated. This is done using the `/sp.tasks` slash command. | Atomic task list with checkpoints/validation steps. |
| **Phase 6: Implementation** | Execute the atomic tasks generated in the previous phase, primarily using the AI with the `/sp.implement` slash command, to generate the **working code**. This phase also generates the **PHRs** (Prompt History Records) as you collaborate with the AI. | Working Code and Prompt History Records (PHRs). |