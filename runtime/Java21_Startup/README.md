# Java21 Startup 01.000.001 — frozen passing snapshot

Title PPSA99877, package SHA256 `33598afb949733eedfc328695d4fffcc81091ed46d1ff92654dc3611cc5d2260`. The maintainer reported ALL PASS on the physical PS5 on2026-11-08 for all four interpreter startup rows. See validation.json for exact evidence and limits.

This snapshot preserves the reviewed source closure at runtime commit `051cbf7e22583d7c11010710d854685f3fb1e731`. Original pinned OpenJDK21 source plus this port closure accompany the passing release; compiled packages are release assets, not source commits. Build in an isolated copy using docs/java21-startup-probe.md. Do not change frozen bytes.

Actual core initialization, JNI_CreateJavaVM, Java arithmetic/UTF16/StrictMath/exceptions, registered JNI calls, a joined Java worker and DestroyJavaVM pass by user report. This does not validate C2, general GC/API/FFM/virtual threads/endurance/performance or Minecraft/mods/shaders.

This root README and validation.json were generated after maintainer acceptance. All other indexed files retain exact source-commit bytes and modes. Existing snapshots and releases remain untouched.
