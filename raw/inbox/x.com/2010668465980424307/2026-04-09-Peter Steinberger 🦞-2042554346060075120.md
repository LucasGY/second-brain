---
title: "RT Magnus Müller: I just realized that Perplexity is built on Browser Use open-source library. Last April, Perplexity users kept reporting that it wa..."
author: "Peter Steinberger 🦞"
date: "2026-04-09 20:31"
isoDate: "2026-04-09T20:31:43.000Z"
source: "https://x.com/steipete/status/2042554346060075120"
tweetId: "2042554346060075120"
images: ["https://pbs.twimg.com/media/HFfTwuDbkAARdkn?format=jpg&name=orig"]
---

# RT Magnus Müller: I just realized that Perplexity is built on Browser Use open-source library. Last April, Perplexity users kept reporting that it wa...

**@Peter Steinberger 🦞** · 2026-04-09 20:31

RT Magnus Müller
I just realized that Perplexity is built on Browser Use open-source library.

Last April, Perplexity users kept reporting that it was randomly searching for “capital of France” and answering “Paris” for unrelated prompts.

That exact prompt, “What is the capital of France?”, is hardcoded in Browser Use. We used it as a sanity check in _verify_llm_connection: every time an Agent() was instantiated, it sent that prompt to the LLM. 

You can disable that but they forgot.

Honestly, if they'd just told us, I'd have happily shown them how to integrate it properly.

Feels like with Manus.

Commit in browser_use: browser_use/agent/service.py lines 1272–1296 at commit 3f4c918a

---

![](https://pbs.twimg.com/media/HFfTwuDbkAARdkn?format=jpg&name=orig)

---
Source: [Tweet](https://x.com/steipete/status/2042554346060075120)
