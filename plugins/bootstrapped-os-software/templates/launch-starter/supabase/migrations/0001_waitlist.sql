-- The waitlist. Only the server writes to it (secret key); nobody can read it from the browser.
create table if not exists public.waitlist (
  email text primary key,
  created_at timestamptz not null default now()
);
alter table public.waitlist enable row level security;
