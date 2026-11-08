# Java17 Startup 01.000.002 — frozen passing snapshot

Title PPSA99876, package SHA-256 `c2241e10bb8c0cb895c7fc02a8490cdd50b2be670e54bc561c90e98c43776c29`. The maintainer reported ALL PASS on the physical PS5 on2026-11-08 for all four startup rows. See validation.json for exact scope.

This snapshot preserves the reviewed source closure at runtime commit `d503c8336d1b4e55faf9e4dc5f147ce596d3ab1d`. The upstream OpenJDK17 source and host/bootstrap/SDK dependencies remain hash/revision pinned; original compiled packages are release assets, not source commits. See docs/java17-startup-probe.md for reproduction. Build in an isolated copy of this snapshot; no frozen bytes should be changed.

Core constructor initialization, real JNI_CreateJavaVM in -Xint mode, Java arithmetic/strings/StrictMath/exceptions, registered JNI calls, a Java worker/join and DestroyJavaVM pass by user report. This does not validate C2, general GC/endurance/performance, Minecraft/mods/shaders or Java21.

This root README and validation.json were generated from the maintainer's acceptance after the source commit. Other indexed files retain exact source-commit bytes/modes. Existing frozen snapshots and original release assets remain unchanged.
