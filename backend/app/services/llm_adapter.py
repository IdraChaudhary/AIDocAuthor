class MockLLM:
    def send(self, prompt: str, context: dict = None) -> str:
        ctx = context or {}
        sec = ctx.get('section') or 'section'
        cur = ctx.get('current') or ''
        # deterministic friendly output
        return f'Generated content for "{sec}". Prompt: {prompt}. Current-length: {len(cur)} chars.'
