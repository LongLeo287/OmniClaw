---
id: github.com-sindresorhus-emittery-d93e2de7-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.378474
---

# KNOWLEDGE EXTRACT: github.com_sindresorhus_emittery_d93e2de7
> **Extracted on:** 2026-04-01 12:02:12
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521668/github.com_sindresorhus_emittery_d93e2de7

---

## File: `.editorconfig`
```
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.yml]
indent_style = space
indent_size = 2
```

## File: `.gitattributes`
```
* text=auto eol=lf
```

## File: `.gitignore`
```
node_modules
yarn.lock
.nyc_output
coverage
```

## File: `.npmrc`
```
package-lock=false
```

## File: `index.d.ts`
```typescript
/**
Emittery accepts strings, symbols, and numbers as event names.

Symbol event names are preferred given that they can be used to avoid name collisions when your classes are extended, especially for internal events.
*/
export type EventName = PropertyKey;

/**
The object passed to every event listener. Always includes `name`. Includes `data` only when the event was emitted with data.

@example
```
import Emittery from 'emittery';

const emitter = new Emittery<{unicorn: string; close: undefined}>();

emitter.on('unicorn', ({name, data}) => {
	console.log(name); //=> 'unicorn'
	console.log(data); //=> '🌈'
});

emitter.on('close', ({name}) => {
	console.log(name); //=> 'close'
});
```
*/
export type EmitteryEvent<Name extends EventName, Data> = [Data] extends [undefined]
	? {readonly name: Name; readonly data?: undefined}
	: {readonly name: Name; readonly data: Data};

type EventDataPair<EventData, Name extends keyof EventData> = Name extends keyof EventData ? EmitteryEvent<Name, EventData[Name]> : never;

// Helper type for turning the passed `EventData` type map into a list of string keys that don't require data alongside the event name when emitting. Uses the same trick that `Omit` does internally to filter keys by building a map of keys to keys we want to keep, and then accessing all the keys to return just the list of keys we want to keep.
type DatalessEventNames<EventData> = {
	[Key in keyof EventData]: EventData[Key] extends undefined ? Key : never;
}[keyof EventData];

declare const listenerAdded: unique symbol;
declare const listenerRemoved: unique symbol;
type OmnipresentEventData = {[listenerAdded]: ListenerChangedData; [listenerRemoved]: ListenerChangedData};

/**
Emittery can collect and log debug information.

To enable this feature set the `DEBUG` environment variable to `emittery` or `*`. Additionally, you can set the static `isDebugEnabled` variable to true on the Emittery class, or `myEmitter.debug.enabled` on an instance of it for debugging a single instance.

See API for more information on how debugging works.
*/
export type DebugLogger<EventData, Name extends keyof EventData> = (type: string, debugName?: string, eventName?: Name, eventData?: EventData[Name]) => void;

/**
Configure debug options of an instance.
*/
export type DebugOptions<EventData> = {
	/**
	Define a name for the instance of Emittery to use when outputting debug data.

	@default undefined

	@example
	```
	import Emittery from 'emittery';

	Emittery.isDebugEnabled = true;

	const emitter = new Emittery({debug: {name: 'myEmitter'}});

	emitter.on('test', () => {
		// …
	});

	emitter.emit('test');
	//=> [16:43:20.417][emittery:subscribe][myEmitter] Event Name: test
	//	data: undefined
	```
	*/
	readonly name?: string;

	/**
	Toggle debug logging just for this instance.

	@default false

	@example
	```
	import Emittery from 'emittery';

	const emitter1 = new Emittery({debug: {name: 'emitter1', enabled: true}});
	const emitter2 = new Emittery({debug: {name: 'emitter2'}});

	emitter1.on('test', () => {
		// …
	});

	emitter2.on('test', () => {
		// …
	});

	emitter1.emit('test');
	//=> [16:43:20.417][emittery:subscribe][emitter1] Event Name: test
	//	data: undefined

	emitter2.emit('test');
	```
	*/
	readonly enabled?: boolean;

	/**
	Function that handles debug data.

	@default
	```
	(type, debugName, eventName, eventData) => {
		try {
			eventData = JSON.stringify(eventData);
		} catch {
			eventData = `Object with the following keys failed to stringify: ${Object.keys(eventData).join(',')}`;
		}

		if (typeof eventName === 'symbol' || typeof eventName === 'number') {
			eventName = eventName.toString();
		}

		const currentTime = new Date();
		const logTime = `${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}.${currentTime.getMilliseconds()}`;
		console.log(`[${logTime}][emittery:${type}][${debugName}] Event Name: ${eventName}\n\tdata: ${eventData}`);
	}
	```

	@example
	```
	import Emittery from 'emittery';

	const myLogger = (type, debugName, eventName, eventData) => {
		console.log(`[${type}]: ${eventName}`);
	};

	const emitter = new Emittery({
		debug: {
			name: 'myEmitter',
			enabled: true,
			logger: myLogger
		}
	});

	emitter.on('test', () => {
		// …
	});

	emitter.emit('test');
	//=> [subscribe]: test
	```
	*/
	readonly logger?: DebugLogger<EventData, keyof EventData>;
};

/**
Configuration options for Emittery.
*/
export type Options<EventData> = {
	readonly debug?: DebugOptions<EventData>;
};

/**
A promise returned from `emittery.once` with an extra `off` method to cancel your subscription.
*/
export type EmitteryOncePromise<T> = {
	off(): void;
} & Promise<T>;

/**
Removes an event subscription.

Can be used with the `using` keyword for automatic cleanup:

@example
```
import Emittery from 'emittery';

const emitter = new Emittery();

{
	using off = emitter.on('event', ({data}) => {
		console.log(data);
	});
	// auto-unsubscribes when leaving scope
}
```
*/
export type UnsubscribeFunction = (() => void) & Disposable;

/**
The data provided as `eventData` when listening for `Emittery.listenerAdded` or `Emittery.listenerRemoved`.
*/
export type ListenerChangedData = {
	/**
	The listener that was added or removed.
	*/
	listener: (event: unknown) => (void | Promise<void>);

	/**
	The name of the event that was added or removed if `.on()` or `.off()` was used, or `undefined` if `.onAny()` or `.offAny()` was used.
	*/
	eventName?: EventName;
};

/**
Emittery is a strictly typed, fully async EventEmitter implementation. Event listeners can be registered with `on` or `once`, and events can be emitted with `emit`.

`Emittery` has a generic `EventData` type that can be provided by users to strongly type the list of events and the data passed to the listeners for those events. Pass an interface of {[eventName]: undefined | <eventArg>}, with all the event names as the keys and the values as the type of the argument passed to listeners if there is one, or `undefined` if there isn't.

@example
```
import Emittery from 'emittery';

const emitter = new Emittery<
	// Pass `{[eventName: <string | symbol | number>]: undefined | <eventArg>}` as the first type argument for events that pass data to their listeners.
	// A value of `undefined` in this map means the event listeners should expect no data, and a type other than `undefined` means the listeners will receive one argument of that type.
	{
		open: string,
		close: undefined
	}
>();

// Typechecks just fine because the data type for the `open` event is `string`.
emitter.emit('open', 'foo\n');

// Typechecks just fine because `close` is present but points to undefined in the event data type map.
emitter.emit('close');

// TS compilation error because `1` isn't assignable to `string`.
emitter.emit('open', 1);

// TS compilation error because `other` isn't defined in the event data type map.
emitter.emit('other');
```
*/
export default class Emittery<
	EventData = Record<EventName, unknown>, AllEventData = EventData & OmnipresentEventData,
	DatalessEvents = DatalessEventNames<EventData>,
> {
	/**
	Toggle debug mode for all instances.

	Default: `true` if the `DEBUG` environment variable is set to `emittery` or `*`, otherwise `false`.

	@example
	```
	import Emittery from 'emittery';

	Emittery.isDebugEnabled = true;

	const emitter1 = new Emittery({debug: {name: 'myEmitter1'}});
	const emitter2 = new Emittery({debug: {name: 'myEmitter2'}});

	emitter1.on('test', () => {
		// …
	});

	emitter2.on('otherTest', () => {
		// …
	});

	emitter1.emit('test');
	//=> [16:43:20.417][emittery:subscribe][myEmitter1] Event Name: test
	//	data: undefined

	emitter2.emit('otherTest');
	//=> [16:43:20.417][emittery:subscribe][myEmitter2] Event Name: otherTest
	//	data: undefined
	```
	*/
	static isDebugEnabled: boolean;

	/**
	Fires when an event listener was added.

	An object with `listener` and `eventName` (if `on` or `off` was used) is provided as event data.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.on(Emittery.listenerAdded, ({data: {listener, eventName}}) => {
		console.log(listener);
		//=> ({data}) => {}

		console.log(eventName);
		//=> '🦄'
	});

	emitter.on('🦄', ({data}) => {
		// Handle data
	});
	```
	*/
	static readonly listenerAdded: typeof listenerAdded;

	/**
	Fires when an event listener was removed.

	An object with `listener` and `eventName` (if `on` or `off` was used) is provided as event data.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	const off = emitter.on('🦄', ({data}) => {
		// Handle data
	});

	emitter.on(Emittery.listenerRemoved, ({data: {listener, eventName}}) => {
		console.log(listener);
		//=> ({data}) => {}

		console.log(eventName);
		//=> '🦄'
	});

	off();
	```
	*/
	static readonly listenerRemoved: typeof listenerRemoved;

	/**
	In TypeScript, it returns a decorator which mixins `Emittery` as property `emitteryPropertyName` and `methodNames`, or all `Emittery` methods if `methodNames` is not defined, into the target class.

	@example
	```
	import Emittery from 'emittery';

	@Emittery.mixin('emittery')
	class MyClass {}

	const instance = new MyClass();

	instance.emit('event');
	```
	*/
	static mixin(
		emitteryPropertyName: string | symbol,
		methodNames?: readonly string[]
	): <T extends abstract new (...arguments_: readonly any[]) => any>(klass: T, context?: ClassDecoratorContext<T>) => T;

	/**
	Debugging options for the current instance.
	*/
	debug: DebugOptions<EventData>;

	/**
	Create a new Emittery instance with the specified options.

	@returns An instance of Emittery that you can use to listen for and emit events.
	*/
	constructor(options?: Options<EventData>);

	/**
	Subscribe to one or more events.

	Using the same listener multiple times for the same event will result in only one method call per emitted event.

	@returns An unsubscribe method, which is also {@link Disposable} (can be used with `using`).

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.on('🦄', ({data}) => {
		console.log(data);
	});

	emitter.on(['🦄', '🐶'], ({name, data}) => {
		console.log(name, data);
	});

	emitter.emit('🦄', '🌈'); // log => '🌈' and '🦄 🌈'
	emitter.emit('🐶', '🍖'); // log => '🐶 🍖'
	```

	@example
	```
	// With AbortSignal
	const abortController = new AbortController();

	emitter.on('🐗', ({data}) => {
		console.log(data);
	}, {signal: abortController.signal});

	abortController.abort();
	```

	@example
	```
	// With `using` for automatic cleanup
	{
		using off = emitter.on('🦄', ({data}) => {
			console.log(data);
		});
		await emitter.emit('🦄', '🌈'); // Logs '🌈'
	}

	await emitter.emit('🦄', '🌈'); // Nothing happens
	```
	*/
	on<Name extends keyof AllEventData>(
		eventName: Name | readonly Name[],
		listener: (event: EventDataPair<AllEventData, Name>) => void | Promise<void>,
		options?: {signal?: AbortSignal}
	): UnsubscribeFunction;

	/**
	Get an async iterator which buffers data each time an event is emitted.

	Call `return()` on the iterator to remove the subscription. You can also pass an {@link AbortSignal} to cancel the subscription externally, or use `await using` for automatic cleanup.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	for await (const {data} of emitter.events('🦄')) {
		console.log(data);

		if (data === '🌈2') {
			break; // Revoke the subscription when we see the value '🌈2'.
		}
	}
	```

	@example
	```
	// With multiple event names
	for await (const {name, data} of emitter.events(['🦄', '🦊'])) {
		console.log(name, data);
	}
	```

	@example
	```
	// With `await using` for automatic cleanup
	{
		await using iterator = emitter.events('🦄');
		for await (const {data} of iterator) {
			console.log(data);
		}
	} // Subscription is automatically revoked
	```
	*/
	events<Name extends keyof EventData>(
		eventName: Name | readonly Name[],
		options?: {signal?: AbortSignal}
	): AsyncIterableIterator<EventDataPair<EventData, Name>> & AsyncDisposable;

	/**
	Remove one or more event subscriptions.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	const listener = ({data}) => {
		console.log(data);
	};

	emitter.on(['🦄', '🐶', '🦊'], listener);
	await emitter.emit('🦄', 'a');
	await emitter.emit('🐶', 'b');
	await emitter.emit('🦊', 'c');
	emitter.off('🦄', listener);
	emitter.off(['🐶', '🦊'], listener);
	await emitter.emit('🦄', 'a'); // Nothing happens
	await emitter.emit('🐶', 'b'); // Nothing happens
	await emitter.emit('🦊', 'c'); // Nothing happens
	```
	*/
	off<Name extends keyof AllEventData>(
		eventName: Name | readonly Name[],
		listener: (event: EventDataPair<AllEventData, Name>) => void | Promise<void>
	): void;

	/**
	Subscribe to one or more events only once. It will be unsubscribed after the first event that matches the predicate (if provided).

	The second argument can be a predicate function or an options object with `predicate` and/or `signal`.

	@returns The promise of event data when `eventName` is emitted and predicate matches (if provided). The promise has an `off` method to cancel the subscription.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	const {data} = await emitter.once('🦄');
	console.log(data);
	//=> '🌈'
	```

	@example
	```
	// With multiple event names
	const {name, data} = await emitter.once(['🦄', '🐶']);
	console.log(name, data);
	```

	@example
	```
	// With predicate
	const event = await emitter.once('data', ({data}) => data.ok === true);
	console.log(event.data);
	//=> {ok: true, value: 42}
	```

	@example
	```
	// With AbortSignal for timeout
	await emitter.once('ready', {signal: AbortSignal.timeout(5000)});
	```

	@example
	```
	// Cancel with .off()
	const promise = emitter.once('🦄');
	promise.off();
	```
	*/
	once<Name extends keyof AllEventData>(
		eventName: Name | readonly Name[],
		predicate?: (event: EventDataPair<AllEventData, Name>) => boolean
	): EmitteryOncePromise<EventDataPair<AllEventData, Name>>;
	once<Name extends keyof AllEventData>(
		eventName: Name | readonly Name[],
		options?: {
			predicate?: (event: EventDataPair<AllEventData, Name>) => boolean;
			signal?: AbortSignal;
		}
	): EmitteryOncePromise<EventDataPair<AllEventData, Name>>;

	/**
	Trigger an event asynchronously, optionally with some data. Listeners are called in the order they were added, but executed concurrently.

	@returns A promise that resolves when all the event listeners are done. *Done* meaning executed if synchronous or resolved when an async/promise-returning function. You usually wouldn't want to wait for this, but you could for example catch possible errors. If any listeners throw/reject, the returned promise rejects with an `AggregateError` — all listener errors are collected in `error.errors`, so no errors are silently lost. All listeners always run to completion, even if some throw or reject.
	*/
	emit<Name extends DatalessEvents>(eventName: Name): Promise<void>;
	emit<Name extends keyof EventData>(
		eventName: Name,
		eventData: EventData[Name]
	): Promise<void>;

	/**
	Same as `emit()`, but it waits for each listener to resolve before triggering the next one. This can be useful if your events depend on each other. Although ideally they should not. Prefer `emit()` whenever possible.

	If any of the listeners throw/reject, the returned promise will be rejected with the error and the remaining listeners will *not* be called.

	@returns A promise that resolves when all the event listeners are done.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.on('🦄', async () => {
		console.log('listener 1 start');
		await new Promise(resolve => setTimeout(resolve, 100));
		console.log('listener 1 done');
	});

	emitter.on('🦄', () => {
		console.log('listener 2'); // Only runs after listener 1 is done
	});

	await emitter.emitSerial('🦄');
	```
	*/
	emitSerial<Name extends DatalessEvents>(eventName: Name): Promise<void>;
	emitSerial<Name extends keyof EventData>(
		eventName: Name,
		eventData: EventData[Name]
	): Promise<void>;

	/**
	Subscribe to be notified about any event.

	@returns A method to unsubscribe, which is also {@link Disposable}.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	const off = emitter.onAny(({name, data}) => {
		console.log(name, data);
	});

	emitter.emit('🦄', '🌈'); // log => '🦄 🌈'

	off();
	```
	*/
	onAny(
		listener: (event: EventDataPair<EventData, keyof EventData>) => void | Promise<void>,
		options?: {signal?: AbortSignal}
	): UnsubscribeFunction;

	/**
	Get an async iterator which buffers an event object each time an event is emitted.

	Call `return()` on the iterator to remove the subscription. You can also pass an {@link AbortSignal} to cancel the subscription externally, or use `await using` for automatic cleanup.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	for await (const {name, data} of emitter.anyEvent()) {
		console.log(name, data);
	}
	```

	@example
	```
	// With `await using` for automatic cleanup
	{
		await using iterator = emitter.anyEvent();
		for await (const {name, data} of iterator) {
			console.log(name, data);
		}
	} // Subscription is automatically revoked
	```
	*/
	anyEvent(options?: {signal?: AbortSignal}): AsyncIterableIterator<EventDataPair<EventData, keyof EventData>> & AsyncDisposable;

	/**
	Remove an `onAny` subscription.
	*/
	offAny(
		listener: (event: EventDataPair<EventData, keyof EventData>) => void | Promise<void>
	): void;

	/**
	Clear all event listeners on the instance.

	If `eventNames` is given, only the listeners for those events are cleared. Accepts a single event name or an array.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.on('🦄', listener);
	emitter.on('🐶', listener);

	emitter.clearListeners('🦄'); // Clear a single event
	emitter.clearListeners(['🐶', '🦊']); // Clear multiple events
	emitter.clearListeners(); // Clear all events
	```
	*/
	clearListeners<Name extends keyof EventData>(eventName?: Name | readonly Name[]): void;

	/**
	Register a function to be called when the first `.on()` listener subscribes to `eventName`. The `initFn` can optionally return a cleanup (deinit) function, which is called when the last `.on()` listener unsubscribes (or when `clearListeners()` removes all listeners for that event).

	If `.on()` listeners already exist when `init()` is called, `initFn` is called immediately.

	Note: Lifecycle hooks only apply to `.on()` listeners. Subscriptions via `.events()` async iterators do not trigger the init or deinit functions.

	@returns An unsubscribe function. Calling it removes the init/deinit hooks, and if the init is currently active, it calls deinit immediately.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.init('mouse', () => {
		terminal.grabInput({mouse: 'button'});

		terminal.on('mouse', (name, data) => {
			emitter.emit('mouse', data);
		});

		return () => {
			terminal.releaseInput();
		};
	});

	// Init is called when the first listener subscribes
	const off = emitter.on('mouse', handler);

	// Adding more listeners does not call init again
	emitter.on('mouse', anotherHandler);

	// Removing one listener does not call deinit yet
	off();

	// Deinit is called when the last listener unsubscribes
	emitter.off('mouse', anotherHandler);
	```

	@example
	```
	// With `using` for automatic cleanup of hooks
	{
		using removeInit = emitter.init('mouse', () => {
			startListening();
			return () => stopListening();
		});
	} // init/deinit hooks are automatically removed
	```
	*/
	init<Name extends keyof EventData>(
		eventName: Name,
		initFn: () => (() => void) | void
	): UnsubscribeFunction;

	/**
	The number of listeners for the `eventName` or all events if not specified.

	@example
	```
	import Emittery from 'emittery';

	const emitter = new Emittery();

	emitter.on('🦄', listener);
	emitter.on('🐶', listener);

	emitter.listenerCount('🦄'); // 1
	emitter.listenerCount(); // 2
	```
	*/
	listenerCount<Name extends keyof EventData>(eventName?: Name | readonly Name[]): number;

	/**
	Log debug information if debug mode is enabled (either globally via `Emittery.isDebugEnabled` or per-instance via `debug.enabled`).
	*/
	logIfDebugEnabled<Name extends keyof EventData>(type: string, eventName?: Name, eventData?: EventData[Name]): void;

	/**
	Bind the given `methodNames`, or all `Emittery` methods if `methodNames` is not defined, into the `target` object.

	@example
	```
	import Emittery from 'emittery';

	const object = {};

	new Emittery().bindMethods(object);

	object.emit('event');
	```
	*/
	bindMethods(target: Record<string, unknown>, methodNames?: readonly string[]): void;
}
```

## File: `index.js`
```javascript
import {
	anyMap,
	producersMap,
	eventsMap,
	lifecycleMap,
} from './maps.js';

const anyProducer = Symbol('anyProducer');
const resolvedPromise = Promise.resolve();

// Define symbols for "meta" events.
const listenerAdded = Symbol('listenerAdded');
const listenerRemoved = Symbol('listenerRemoved');

const metaEventsAllowed = new WeakMap();
const metaEventsPermitted = new WeakMap();
const suppressAllEnqueue = Symbol('suppressAllEnqueue');
const suppressedEventsMap = new WeakMap();
let isGlobalDebugEnabled = false;

const isEventKeyType = key => typeof key === 'string' || typeof key === 'symbol' || typeof key === 'number';

function makeDisposable(function_) {
	function_[Symbol.dispose] = function_;
	return function_;
}

function addAbortListener(signal, listener, {swallowErrors = false} = {}) {
	if (!signal) {
		return () => {};
	}

	const onAbort = () => {
		if (swallowErrors) {
			try {
				listener();
			} catch {}

			return;
		}

		listener();
	};

	if (signal.aborted) {
		onAbort();
		return () => {};
	}

	signal.addEventListener('abort', onAbort, {once: true});

	return () => {
		signal.removeEventListener('abort', onAbort);
	};
}

function assertEventName(eventName) {
	if (!isEventKeyType(eventName)) {
		throw new TypeError('`eventName` must be a string, symbol, or number');
	}
}

function assertListener(listener) {
	if (typeof listener !== 'function') {
		throw new TypeError('listener must be a function');
	}
}

function getListeners(instance, eventName) {
	const events = eventsMap.get(instance);
	if (!events.has(eventName)) {
		return;
	}

	return events.get(eventName);
}

function getEventProducers(instance, eventName) {
	const key = isEventKeyType(eventName) ? eventName : anyProducer;
	const producers = producersMap.get(instance);
	if (!producers.has(key)) {
		return;
	}

	return producers.get(key);
}

function enqueueProducers(instance, eventName, eventData, hasEventData) {
	if (isEnqueueSuppressed(instance, eventName)) {
		return;
	}

	const producers = producersMap.get(instance);
	if (!producers.has(eventName) && !producers.get(anyProducer)?.size) {
		return;
	}

	const resolvedEventData = Promise.resolve(eventData);
	const makeEvent = async () => makeEventObject(eventName, await resolvedEventData, hasEventData);

	if (producers.has(eventName)) {
		for (const producer of producers.get(eventName)) {
			producer.enqueue(makeEvent());
		}
	}

	if (producers.has(anyProducer)) {
		for (const producer of producers.get(anyProducer)) {
			producer.enqueue(makeEvent());
		}
	}
}

function iterator(instance, eventNames, {signal} = {}) {
	eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];

	let isFinished = false;
	let flush = () => {};
	let queue = [];
	let removeAbortListener = () => {};

	const producer = {
		enqueue(item) {
			queue.push(item);
			flush();
		},
		finish() {
			isFinished = true;
			removeAbortListener();
			flush();
		},
	};

	for (const eventName of eventNames) {
		const producerKey = isEventKeyType(eventName) ? eventName : anyProducer;
		let set = getEventProducers(instance, eventName);
		if (!set) {
			set = new Set();
			const producers = producersMap.get(instance);
			producers.set(producerKey, set);
		}

		set.add(producer);
	}

	const removeProducer = () => {
		for (const eventName of eventNames) {
			const producerKey = isEventKeyType(eventName) ? eventName : anyProducer;
			const set = getEventProducers(instance, eventName);
			if (set) {
				set.delete(producer);
				if (set.size === 0) {
					const producers = producersMap.get(instance);
					producers.delete(producerKey);
				}
			}
		}
	};

	const stop = () => {
		if (!queue) {
			return;
		}

		queue = undefined;
		removeAbortListener();

		removeProducer();
		flush();
	};

	removeAbortListener = addAbortListener(signal, stop);

	return {
		async next() {
			if (!queue) {
				return {done: true};
			}

			if (queue.length === 0) {
				if (isFinished) {
					stop();
					return this.next();
				}

				const {promise, resolve} = Promise.withResolvers();
				flush = resolve;
				await promise;

				return this.next();
			}

			return {
				done: false,
				value: await queue.shift(),
			};
		},

		async return(value) {
			stop();

			return arguments.length > 0
				? {done: true, value: await value}
				: {done: true};
		},

		[Symbol.asyncIterator]() {
			return this;
		},

		async [Symbol.asyncDispose]() {
			await this.return();
		},
	};
}

function defaultMethodNamesOrAssert(methodNames) {
	if (methodNames === undefined) {
		return allEmitteryMethods;
	}

	if (!Array.isArray(methodNames)) {
		throw new TypeError('`methodNames` must be an array of strings');
	}

	for (const methodName of methodNames) {
		if (!allEmitteryMethods.includes(methodName)) {
			if (typeof methodName !== 'string') {
				throw new TypeError('`methodNames` element must be a string');
			}

			throw new Error(`${methodName} is not Emittery method`);
		}
	}

	return methodNames;
}

const isMetaEvent = eventName => eventName === listenerAdded || eventName === listenerRemoved;

function withSuppressedEnqueue(instance, eventNames, function_) {
	const keys = eventNames.some(name => !isEventKeyType(name))
		? [suppressAllEnqueue]
		: eventNames;

	let suppressed = suppressedEventsMap.get(instance);
	if (!suppressed) {
		suppressed = new Set();
		suppressedEventsMap.set(instance, suppressed);
	}

	// Track only the keys we actually added, so re-entrant calls don't prematurely lift suppression.
	const added = [];
	for (const key of keys) {
		if (!suppressed.has(key)) {
			suppressed.add(key);
			added.push(key);
		}
	}

	try {
		return function_();
	} finally {
		for (const key of added) {
			suppressed.delete(key);
		}

		if (suppressed.size === 0) {
			suppressedEventsMap.delete(instance);
		}
	}
}

function isEnqueueSuppressed(instance, eventName) {
	const suppressed = suppressedEventsMap.get(instance);
	if (!suppressed) {
		return false;
	}

	return suppressed.has(suppressAllEnqueue) || suppressed.has(eventName);
}

function callInitFn(instance, lifecycle, listener, {eventName, set}) {
	try {
		const result = lifecycle.initFn();
		if (typeof result === 'function') {
			lifecycle.deinitFn = result;
		}
	} catch (error) {
		set.delete(listener);
		if (set.size === 0) {
			eventsMap.get(instance).delete(eventName);
		}

		throw error;
	}
}

function callAndUnsetDeinitFn(lifecycle) {
	const deinitFn = lifecycle?.deinitFn;
	if (deinitFn) {
		lifecycle.deinitFn = undefined;
		deinitFn();
	}
}

const subscribeAction = 'subscribe';
const unsubscribeAction = 'unsubscribe';

function transitionEventListener(instance, {eventName, listener, action, swallowLifecycleError = false, removeResubscribedListener = false}) {
	if (action === subscribeAction) {
		let set = getListeners(instance, eventName);
		if (!set) {
			set = new Set();
			eventsMap.get(instance).set(eventName, set);
		}

		const wasEmpty = set.size === 0;
		const alreadyListening = set.has(listener);
		set.add(listener);

		if (!isMetaEvent(eventName) && wasEmpty && !isEnqueueSuppressed(instance, eventName)) {
			const lifecycle = lifecycleMap.get(instance).get(eventName);
			if (lifecycle) {
				callInitFn(instance, lifecycle, listener, {eventName, set});
			}
		}

		return {hasSet: true, changed: !alreadyListening};
	}

	const set = getListeners(instance, eventName);
	if (!set) {
		return {hasSet: false, changed: false};
	}

	const removed = set.delete(listener);
	if (set.size === 0) {
		eventsMap.get(instance).delete(eventName);

		const lifecycle = lifecycleMap.get(instance).get(eventName);
		if (swallowLifecycleError) {
			try {
				callAndUnsetDeinitFn(lifecycle);
			} catch {}
		} else {
			callAndUnsetDeinitFn(lifecycle);
		}

		if (removeResubscribedListener) {
			// Deinit can re-subscribe the same listener; keep rollback authoritative.
			const setAfterDeinit = getListeners(instance, eventName);
			setAfterDeinit?.delete(listener);
			if (setAfterDeinit?.size === 0) {
				eventsMap.get(instance).delete(eventName);
			}
		}
	}

	return {hasSet: true, changed: removed};
}

function emitSubscriptionSideEffects(instance, {eventName, listener, action, swallowErrors = false}) {
	const isSubscribe = action === subscribeAction;
	const debugType = isSubscribe ? 'subscribe' : 'unsubscribe';
	const metaEvent = isSubscribe ? listenerAdded : listenerRemoved;

	if (swallowErrors) {
		try {
			instance.logIfDebugEnabled(debugType, eventName, undefined);
		} catch {}

		if (!isMetaEvent(eventName)) {
			try {
				emitMetaEvent(instance, metaEvent, {eventName, listener});
			} catch {}
		}

		return;
	}

	instance.logIfDebugEnabled(debugType, eventName, undefined);

	if (!isMetaEvent(eventName)) {
		emitMetaEvent(instance, metaEvent, {eventName, listener});
	}
}

function rollbackAddedListeners(instance, eventNames, listener) {
	withSuppressedEnqueue(instance, eventNames, () => {
		for (const eventName of eventNames) {
			const {hasSet} = transitionEventListener(instance, {
				eventName,
				listener,
				action: unsubscribeAction,
				swallowLifecycleError: true,
				removeResubscribedListener: true,
			});
			if (!hasSet) {
				continue;
			}

			emitSubscriptionSideEffects(instance, {
				eventName,
				listener,
				action: unsubscribeAction,
				swallowErrors: true,
			});
		}
	});
}

function finishAndClearProducers(instance, eventName) {
	const producers = getEventProducers(instance, eventName);
	if (producers) {
		for (const producer of producers) {
			producer.finish();
		}

		producers.clear();
	}
}

function finishAndClearAllProducers(instance) {
	const allProducers = producersMap.get(instance);
	for (const [key, producers] of allProducers.entries()) {
		for (const producer of producers) {
			producer.finish();
		}

		producers.clear();
		allProducers.delete(key);
	}
}

const makeEventObject = (eventName, eventData, hasEventData) =>
	hasEventData ? {name: eventName, data: eventData} : {name: eventName};

function emitMetaEvent(emitter, eventName, eventData) {
	metaEventsAllowed.set(emitter, (metaEventsAllowed.get(emitter) ?? 0) + 1);
	metaEventsPermitted.set(emitter, (metaEventsPermitted.get(emitter) ?? 0) + 1);
	try {
		Emittery.prototype.emit.call(emitter, eventName, eventData);
	} finally {
		metaEventsAllowed.set(emitter, (metaEventsAllowed.get(emitter) ?? 0) - 1);
	}
}

export default class Emittery {
	static mixin(emitteryPropertyName, methodNames) {
		methodNames = defaultMethodNamesOrAssert(methodNames);
		return (target, _context) => {
			if (typeof target !== 'function') {
				throw new TypeError('`target` must be function');
			}

			for (const methodName of methodNames) {
				if (target.prototype[methodName] !== undefined) {
					throw new Error(`The property \`${methodName}\` already exists on \`target\``);
				}
			}

			function getEmitteryProperty() {
				Object.defineProperty(this, emitteryPropertyName, {
					enumerable: false,
					value: new Emittery(),
				});
				return this[emitteryPropertyName];
			}

			Object.defineProperty(target.prototype, emitteryPropertyName, {
				enumerable: false,
				get: getEmitteryProperty,
			});

			const emitteryMethodCaller = methodName => function (...args) {
				return this[emitteryPropertyName][methodName](...args);
			};

			for (const methodName of methodNames) {
				Object.defineProperty(target.prototype, methodName, {
					enumerable: false,
					value: emitteryMethodCaller(methodName),
				});
			}

			return target;
		};
	}

	static get isDebugEnabled() {
		// In a browser environment, `globalThis.process` can potentially reference a DOM Element with a `#process` ID,
		// so instead of just type checking `globalThis.process`, we need to make sure that `globalThis.process.env` exists.
		// eslint-disable-next-line n/prefer-global/process
		if (typeof globalThis.process?.env !== 'object') {
			return isGlobalDebugEnabled;
		}

		// eslint-disable-next-line n/prefer-global/process
		const {env} = globalThis.process ?? {env: {}};
		return env.DEBUG === 'emittery' || env.DEBUG === '*' || isGlobalDebugEnabled;
	}

	static set isDebugEnabled(newValue) {
		isGlobalDebugEnabled = newValue;
	}

	constructor(options = {}) {
		anyMap.set(this, new Set());
		eventsMap.set(this, new Map());
		producersMap.set(this, new Map());
		lifecycleMap.set(this, new Map());

		producersMap.get(this).set(anyProducer, new Set());

		for (const methodName of allEmitteryMethods) {
			Object.defineProperty(this, methodName, {
				value: this[methodName].bind(this),
				writable: true,
				enumerable: false,
				configurable: true,
			});
		}

		this.debug = options.debug ?? {};

		if (this.debug.enabled === undefined) {
			this.debug.enabled = false;
		}

		this.debug.logger ||= (type, debugName, eventName, eventData) => {
			try {
				// TODO: Use https://github.com/sindresorhus/safe-stringify when the package is more mature. Just copy-paste the code.
				eventData = JSON.stringify(eventData);
			} catch {
				eventData = `Object with the following keys failed to stringify: ${Object.keys(eventData).join(',')}`;
			}

			if (typeof eventName === 'symbol' || typeof eventName === 'number') {
				eventName = eventName.toString();
			}

			const currentTime = new Date();
			const logTime = `${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}.${currentTime.getMilliseconds()}`;
			console.log(`[${logTime}][emittery:${type}][${debugName}] Event Name: ${eventName}\n\tdata: ${eventData}`);
		};
	}

	logIfDebugEnabled(type, eventName, eventData) {
		if (Emittery.isDebugEnabled || this.debug.enabled) {
			this.debug.logger(type, this.debug.name, eventName, eventData);
		}
	}

	on(eventNames, listener, {signal} = {}) {
		assertListener(listener);

		eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];
		const addedEventNames = [];
		try {
			for (const eventName of eventNames) {
				assertEventName(eventName);
				const {changed} = transitionEventListener(this, {
					eventName,
					listener,
					action: subscribeAction,
				});
				if (changed) {
					addedEventNames.push(eventName);
				}

				emitSubscriptionSideEffects(this, {
					eventName,
					listener,
					action: subscribeAction,
				});
			}
		} catch (error) {
			rollbackAddedListeners(this, addedEventNames, listener);
			throw error;
		}

		let removeAbortListener = () => {};
		const noError = Symbol('no-error');
		const off = () => {
			removeAbortListener();
			let firstError = noError;

			for (const eventName of eventNames) {
				try {
					this.off(eventName, listener);
				} catch (error) {
					firstError = firstError === noError ? error : firstError;
				}
			}

			if (firstError !== noError) {
				throw firstError;
			}
		};

		removeAbortListener = addAbortListener(signal, off, {swallowErrors: true});

		return makeDisposable(off);
	}

	off(eventNames, listener) {
		assertListener(listener);

		eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];
		for (const eventName of eventNames) {
			assertEventName(eventName);
			transitionEventListener(this, {
				eventName,
				listener,
				action: unsubscribeAction,
			});
			emitSubscriptionSideEffects(this, {
				eventName,
				listener,
				action: unsubscribeAction,
			});
		}
	}

	once(eventNames, predicateOrOptions) {
		const {promise, resolve, reject} = Promise.withResolvers();
		let off = () => {};
		let signal;
		let isSettled = false;
		let removeAbortListener = () => {};
		eventNames = Array.isArray(eventNames) ? [...eventNames] : [eventNames];

		try {
			let predicate;

			if (typeof predicateOrOptions === 'function') {
				predicate = predicateOrOptions;
			} else if (typeof predicateOrOptions === 'object' && predicateOrOptions !== null) {
				predicate = predicateOrOptions.predicate;
				signal = predicateOrOptions.signal;
			} else if (predicateOrOptions !== undefined) {
				throw new TypeError('predicate must be a function');
			}

			if (predicate !== undefined && typeof predicate !== 'function') {
				throw new TypeError('predicate must be a function');
			}

			if (signal?.aborted) {
				throw signal.reason;
			}

			let listener = () => {};
			const unsubscribe = () => {
				removeAbortListener();
				const noError = Symbol('no-error');
				let firstError = noError;

				for (const eventName of eventNames) {
					try {
						this.off(eventName, listener);
					} catch (error) {
						firstError = firstError === noError ? error : firstError;
					}
				}

				if (firstError !== noError) {
					throw firstError;
				}
			};

			const unsubscribeAndSettle = () => {
				unsubscribe();
				isSettled = true;
			};

			listener = event => {
				if (predicate && !predicate(event)) {
					return;
				}

				if (isSettled) {
					return;
				}

				try {
					unsubscribeAndSettle();
				} catch (error) {
					reject(error);
					return;
				}

				resolve(event);
			};

			this.on(eventNames, listener);
			off = unsubscribe;

			removeAbortListener = addAbortListener(signal, () => {
				if (isSettled) {
					return;
				}

				try {
					unsubscribeAndSettle();
				} catch {}

				isSettled = true;
				reject(signal.reason);
			});

			promise.off = () => {
				if (isSettled) {
					return;
				}

				unsubscribeAndSettle();
			};
		} catch (error) {
			reject(error);
		}

		if (promise.off === undefined) {
			promise.off = off;
		}

		return promise;
	}

	events(eventNames, {signal} = {}) {
		eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];
		for (const eventName of eventNames) {
			assertEventName(eventName);
		}

		return iterator(this, eventNames, {signal});
	}

	async emit(eventName, eventData) {
		assertEventName(eventName);

		if (isMetaEvent(eventName)) {
			const remainingPermits = metaEventsPermitted.get(this) ?? 0;
			if ((metaEventsAllowed.get(this) ?? 0) === 0 || remainingPermits === 0) {
				throw new TypeError('`eventName` cannot be meta event `listenerAdded` or `listenerRemoved`');
			}

			metaEventsPermitted.set(this, remainingPermits - 1);
		}

		if (!isMetaEvent(eventName)) {
			this.logIfDebugEnabled('emit', eventName, eventData);
		}

		const hasEventData = arguments.length > 1;

		enqueueProducers(this, eventName, eventData, hasEventData);

		const listeners = getListeners(this, eventName) ?? new Set();
		const anyListeners = anyMap.get(this);
		const staticListeners = [...listeners];
		const staticAnyListeners = isMetaEvent(eventName) ? [] : [...anyListeners];

		await resolvedPromise;
		const results = await Promise.allSettled([
			...staticListeners.map(async listener => {
				if (listeners.has(listener)) {
					return listener(makeEventObject(eventName, eventData, hasEventData));
				}
			}),
			...staticAnyListeners.map(async listener => {
				if (anyListeners.has(listener)) {
					return listener(makeEventObject(eventName, eventData, hasEventData));
				}
			}),
		]);

		const errors = results.values()
			.filter(result => result.status === 'rejected')
			.map(result => result.reason)
			.toArray();

		if (errors.length > 0) {
			throw new AggregateError(errors, 'One or more listeners threw an error');
		}
	}

	async emitSerial(eventName, eventData) {
		assertEventName(eventName);

		if (isMetaEvent(eventName)) {
			const remainingPermits = metaEventsPermitted.get(this) ?? 0;
			if ((metaEventsAllowed.get(this) ?? 0) === 0 || remainingPermits === 0) {
				throw new TypeError('`eventName` cannot be meta event `listenerAdded` or `listenerRemoved`');
			}

			metaEventsPermitted.set(this, remainingPermits - 1);
		}

		if (!isMetaEvent(eventName)) {
			this.logIfDebugEnabled('emitSerial', eventName, eventData);
		}

		const hasEventData = arguments.length > 1;

		enqueueProducers(this, eventName, eventData, hasEventData);

		const listeners = getListeners(this, eventName) ?? new Set();
		const anyListeners = anyMap.get(this);
		const staticListeners = [...listeners];
		const staticAnyListeners = isMetaEvent(eventName) ? [] : [...anyListeners];

		await resolvedPromise;
		/* eslint-disable no-await-in-loop */
		for (const listener of staticListeners) {
			if (listeners.has(listener)) {
				await listener(makeEventObject(eventName, eventData, hasEventData));
			}
		}

		for (const listener of staticAnyListeners) {
			if (anyListeners.has(listener)) {
				await listener(makeEventObject(eventName, eventData, hasEventData));
			}
		}
		/* eslint-enable no-await-in-loop */
	}

	onAny(listener, {signal} = {}) {
		assertListener(listener);

		this.logIfDebugEnabled('subscribeAny', undefined, undefined);

		anyMap.get(this).add(listener);
		emitMetaEvent(this, listenerAdded, {listener});

		let removeAbortListener = () => {};
		const offAny = () => {
			removeAbortListener();
			this.offAny(listener);
		};

		removeAbortListener = addAbortListener(signal, offAny, {swallowErrors: true});

		return makeDisposable(offAny);
	}

	anyEvent({signal} = {}) {
		return iterator(this, undefined, {signal});
	}

	offAny(listener) {
		assertListener(listener);

		this.logIfDebugEnabled('unsubscribeAny', undefined, undefined);

		emitMetaEvent(this, listenerRemoved, {listener});
		anyMap.get(this).delete(listener);
	}

	clearListeners(eventNames) {
		eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];
		const shouldClearAll = eventNames.some(eventName => !isEventKeyType(eventName));

		withSuppressedEnqueue(this, eventNames, () => {
			const noError = Symbol('no-error');
			let firstError = noError;

			try {
				for (const eventName of eventNames) {
					try {
						this.logIfDebugEnabled('clear', eventName, undefined);
					} catch (error) {
						firstError = firstError === noError ? error : firstError;
					}

					if (isEventKeyType(eventName)) {
						const set = getListeners(this, eventName);
						const hadListeners = set?.size > 0;
						set?.clear();
						finishAndClearProducers(this, eventName);

						const lifecycle = hadListeners ? lifecycleMap.get(this).get(eventName) : undefined;
						try {
							callAndUnsetDeinitFn(lifecycle);
						} catch (error) {
							firstError = firstError === noError ? error : firstError;
						}
					} else {
						anyMap.get(this).clear();
						finishAndClearAllProducers(this);

						for (const [eventName, listeners] of eventsMap.get(this).entries()) {
							const hadListeners = listeners.size > 0;
							listeners.clear();

							const lifecycle = hadListeners ? lifecycleMap.get(this).get(eventName) : undefined;
							try {
								callAndUnsetDeinitFn(lifecycle);
							} catch (error) {
								firstError = firstError === noError ? error : firstError;
							}

							// Re-clear in case deinit re-subscribed.
							listeners.clear();
							eventsMap.get(this).delete(eventName);
						}

						// Re-clear in case deinit re-subscribed to onAny() or created new iterators.
						anyMap.get(this).clear();
						finishAndClearAllProducers(this);
					}
				}
			} finally {
				if (shouldClearAll) {
					anyMap.get(this).clear();
					for (const listeners of eventsMap.get(this).values()) {
						listeners.clear();
					}

					eventsMap.get(this).clear();
					finishAndClearAllProducers(this);
				} else {
					// Final re-clear for cross-event deinit re-subscription (e.g., deinit for B re-subscribes to A).
					for (const eventName of eventNames) {
						if (isEventKeyType(eventName)) {
							const set = getListeners(this, eventName);
							set?.clear();
							eventsMap.get(this).delete(eventName);
							finishAndClearProducers(this, eventName);
						}
					}
				}
			}

			if (firstError !== noError) {
				throw firstError;
			}
		});
	}

	init(eventName, initFn) {
		assertEventName(eventName);

		if (isMetaEvent(eventName)) {
			throw new TypeError('`eventName` cannot be a meta event');
		}

		if (typeof initFn !== 'function') {
			throw new TypeError('`initFn` must be a function');
		}

		const lifecycles = lifecycleMap.get(this);

		if (lifecycles.has(eventName)) {
			throw new Error('`eventName` already has an init function registered');
		}

		const lifecycle = {initFn, deinitFn: undefined};
		lifecycles.set(eventName, lifecycle);

		// If listeners already exist, call init immediately
		const existingListeners = getListeners(this, eventName);
		if (existingListeners?.size > 0) {
			try {
				const result = initFn();
				if (typeof result === 'function') {
					lifecycle.deinitFn = result;
				}
			} catch (error) {
				lifecycles.delete(eventName);
				throw error;
			}
		}

		return makeDisposable(() => {
			try {
				callAndUnsetDeinitFn(lifecycle);
			} finally {
				if (lifecycles.get(eventName) === lifecycle) {
					lifecycles.delete(eventName);
				}
			}
		});
	}

	listenerCount(eventNames) {
		eventNames = Array.isArray(eventNames) ? eventNames : [eventNames];
		let count = 0;

		for (const eventName of eventNames) {
			if (isEventKeyType(eventName)) {
				count += anyMap.get(this).size
					+ (getListeners(this, eventName)?.size ?? 0)
					+ (getEventProducers(this, eventName)?.size ?? 0)
					+ (getEventProducers(this)?.size ?? 0);

				continue;
			}

			if (eventName !== undefined) {
				assertEventName(eventName);
			}

			count += anyMap.get(this).size;

			for (const value of eventsMap.get(this).values()) {
				count += value.size;
			}

			for (const value of producersMap.get(this).values()) {
				count += value.size;
			}
		}

		return count;
	}

	bindMethods(target, methodNames) {
		if (!target || typeof target !== 'object') {
			throw new TypeError('`target` must be an object');
		}

		methodNames = defaultMethodNamesOrAssert(methodNames);

		for (const methodName of methodNames) {
			if (target[methodName] !== undefined) {
				throw new Error(`The property \`${methodName}\` already exists on \`target\``);
			}

			Object.defineProperty(target, methodName, {
				enumerable: false,
				value: this[methodName].bind(this),
			});
		}
	}
}

const allEmitteryMethods = Object.getOwnPropertyNames(Emittery.prototype).filter(v => v !== 'constructor');

Object.defineProperty(Emittery, 'listenerAdded', {
	value: listenerAdded,
	writable: false,
	enumerable: true,
	configurable: false,
});
Object.defineProperty(Emittery, 'listenerRemoved', {
	value: listenerRemoved,
	writable: false,
	enumerable: true,
	configurable: false,
});
```

## File: `index.test-d.ts`
```typescript
/* eslint-disable @typescript-eslint/no-empty-function, @typescript-eslint/no-floating-promises */
import {
	expectType,
	expectError,
	expectNotAssignable,
	expectAssignable,
} from 'tsd';
import {pEventIterator} from 'p-event';
import Emittery, {type EmitteryEvent, type EventName} from './index.js';

type AnyListener = (event: unknown) => void | Promise<void>;

// Emit
{
	const ee = new Emittery<{anEvent: undefined}>();
	ee.emit('anEvent');
	const ee2 = new Emittery<{anEvent: string}>();
	ee2.emit('anEvent', 'some data');
}

// On
{
	const ee = new Emittery();
	ee.on('anEvent', () => undefined);
	ee.on('anEvent', async () => {});
	ee.on('anEvent', event => undefined);
	ee.on('anEvent', async event => {});
	ee.on('anEvent', async event => {}, {signal: new AbortController().signal});
	ee.on(['anEvent', 'anotherEvent'], async event => undefined);
	ee.on(Emittery.listenerAdded, ({data: {eventName, listener}}) => {
		expectType<PropertyKey | undefined>(eventName);
		expectType<AnyListener>(listener);
	});
	ee.on(Emittery.listenerRemoved, ({data: {eventName, listener}}) => {
		expectType<PropertyKey | undefined>(eventName);
		expectType<AnyListener>(listener);
	});
}

// Off
{
	const ee = new Emittery();
	ee.off('anEvent', () => undefined);
	ee.off('anEvent', async () => {});
	ee.off('anEvent', event => undefined);
	ee.off('anEvent', async event => {});
	ee.off(Emittery.listenerAdded, ({data: {eventName, listener}}) => {});
	ee.off(Emittery.listenerRemoved, ({data: {eventName, listener}}) => {});
}

// Once
{
	const ee = new Emittery();
	const test = async () => {
		await ee.once('anEvent');
		const listenerAddedEvent = await ee.once(Emittery.listenerAdded);
		expectType<PropertyKey | undefined>(listenerAddedEvent.data.eventName);
		expectType<AnyListener>(listenerAddedEvent.data.listener);
		const listenerRemovedEvent = await ee.once(Emittery.listenerRemoved);
		expectType<PropertyKey | undefined>(listenerRemovedEvent.data.eventName);
		expectType<AnyListener>(listenerRemovedEvent.data.listener);
		const oncePromise = ee.once('anotherEvent');
		oncePromise.off();
		await oncePromise;
	};
}

{
	const ee = new Emittery();
	expectError(ee.emit('anEvent', 'some data', 'and more'));
}

{
	const ee = new Emittery();
	expectError(ee.on('anEvent', (data: any, more: any) => undefined));
}

// IsDebug
{
	type MyEventData = {
		value: string;
		open: undefined;
		close: boolean;
	};

	const ee = new Emittery<MyEventData>();

	const myLogger = (type: string, debugName?: string, eventName?: keyof MyEventData, eventData?: MyEventData[keyof MyEventData]): void => {
		expectAssignable<string>(type);
		expectAssignable<string | undefined>(debugName);
		expectAssignable<string | undefined>(eventName);
		expectAssignable<MyEventData[keyof MyEventData]>(eventData);
	};

	const debugOptions = {name: 'test', enabled: true, logger: myLogger};
	const emitterWithEnabledDebugOnly = new Emittery<MyEventData>({debug: {enabled: true}});
	const unsafeLogger = (type: string, debugName: string): void => {
		expectAssignable<string>(type);
		expectAssignable<string>(debugName);
	};

	expectError(new Emittery<MyEventData>({debug: {enabled: true, logger: unsafeLogger}}));

	// Global debug flag
	expectAssignable<boolean>(Emittery.isDebugEnabled);

	// General debug options
	expectAssignable<typeof ee.debug>(debugOptions);
	expectAssignable<Emittery<MyEventData>>(emitterWithEnabledDebugOnly);
	expectAssignable<string | undefined>(ee.debug.name);
	expectAssignable<boolean | undefined>(ee.debug.enabled);

	// Debug logger
	expectNotAssignable<() => undefined>(ee.debug.logger);
	expectNotAssignable<(data: unknown) => undefined>(ee.debug.logger);
	expectNotAssignable<(type: string, debugName: number) => undefined>(ee.debug.logger);
	expectNotAssignable<((type: string, debugName?: number, eventName?: string, eventData?: Record<string, any>) => void) | undefined>(ee.debug.logger);
	expectAssignable<typeof ee.debug.logger>(myLogger);
}

// Strict typing for emission
{
	const ee = new Emittery<{
		value: string;
		open: undefined;
		close: undefined;
	}>();
	ee.emit('open');
	ee.emit('close');
	ee.emit('value', 'test');
	expectError(ee.emit('value'));
	expectError(ee.emit('open', 'test'));
}

// Strict typing for listeners
{
	const ee = new Emittery<{
		value: string;
		open: undefined;
		close: undefined;
		other: number;
		maybe: string | undefined;
	}>();
	ee.on('open', () => {});
	ee.on('open', event => {
		expectType<EmitteryEvent<'open', undefined>>(event);
		expectAssignable<{name: 'open'; data?: undefined}>(event);
		expectNotAssignable<{name: 'open'; data: undefined}>(event);
	});
	ee.on('open', ({data}) => {
		expectType<undefined>(data);
	});

	ee.on('value', () => {});
	ee.on('value', ({data}) => {
		expectType<string>(data);
	});
	ee.on(['value', 'other'], ({name, data}) => {
		expectType<'value' | 'other'>(name);
		expectType<string | number>(data);
	});
	ee.on(['value', 'other'], event => {
		if (event.name === 'value') {
			expectType<string>(event.data);
		} else {
			expectType<number>(event.data);
		}
	});
	ee.on('maybe', event => {
		expectType<string | undefined>(event.data);
	});
	const listener = ({data}: EmitteryEvent<'value', string>) => undefined;
	ee.on('value', listener);
	ee.off('value', listener);
	const test = async () => {
		const event = await ee.once('value');
		expectType<EmitteryEvent<'value', string>>(event);
		const multiEvent = await ee.once(['value', 'other']);
		expectType<EmitteryEvent<'value', string> | EmitteryEvent<'other', number>>(multiEvent);
	};

	expectError(ee.on('value', (value: number) => {}));
}

// Async listeners
{
	const ee = new Emittery<{
		open: undefined;
		close: string;
	}>();
	ee.on('open', () => {});
	ee.on('open', async () => {});
	ee.on('open', async () => {});
	ee.on('close', async ({data}) => {
		expectType<string>(data);
	});
}

// Strict typing for onAny, offAny listeners
{
	const ee = new Emittery<{
		value: string;
		open: undefined;
		close: undefined;
		other: number;
	}>();

	ee.onAny(event => {
		// Some events are dataless so `data` only exists on some union variants
		expectType<'value' | 'open' | 'close' | 'other'>(event.name);
	});

	ee.onAny(() => {}, {signal: new AbortController().signal});

	const listener = ({name}: {name: string}) => {};
	ee.onAny(listener);
	ee.offAny(listener);
}

// Strict typing for onAny, offAny listeners for an Emittery that only has listeners with arguments
{
	const ee = new Emittery<{
		value: string;
		other: number;
	}>();

	ee.onAny(({name, data}) => {
		expectType<'value' | 'other'>(name);
		expectType<string | number>(data);
	});
}

// Strict typing for anyEvent iterator
{
	const testAnyEvent = async () => {
		const ee = new Emittery<{
			value: string;
			open: undefined;
			close: undefined;
		}>();

		for await (const event of ee.anyEvent()) {
			expectType<'value' | 'open' | 'close'>(event.name);
		}

		const ee2 = new Emittery<{
			value: string;
			other: number;
		}>();

		for await (const event of ee2.anyEvent()) {
			expectType<'value' | 'other'>(event.name);
			expectType<string | number>(event.data);
		}
	};
}

// Strict typing for `.events` iterator
{
	const testEventsIterator = async () => {
		const ee = new Emittery<{
			value: string;
			open: undefined;
			close: undefined;
			other: number;
		}>();

		for await (const event of ee.events('value')) {
			expectType<string>(event.data);
			expectType<'value'>(event.name);
		}

		for await (const event of ee.events(['value', 'other'])) {
			expectType<'value' | 'other'>(event.name);
			expectType<string | number>(event.data);
		}

		for await (const event of ee.events(['value', 'open'])) {
			expectType<'value' | 'open'>(event.name);
		}

		const ee2 = new Emittery();
		for await (const event of ee2.events('unknown')) {
			expectAssignable<{name: EventName}>(event);
		}
	};
}

// Compatibility with p-event, without explicit types
{
	const ee = new Emittery();
	pEventIterator(ee, 'data', {
		resolutionEvents: ['finish'],
	});
}

// Compatibility with p-event, with explicit types
{
	type EventData = {
		data: unknown;
		error: unknown;
		finish: undefined;
	};
	const ee = new Emittery<EventData>();
	pEventIterator<keyof EventData, unknown>(ee, 'data', {
		resolutionEvents: ['finish'],
	});
}

// Mixin - return type is preserved as T
class MixinBase {
	test() {}
}

expectType<typeof MixinBase>(Emittery.mixin('emittery')(MixinBase));

// Mixin - works with parameterized constructor
Emittery.mixin('emittery')(class { // eslint-disable-line @typescript-eslint/no-extraneous-class
	constructor(argument: string) {} // eslint-disable-line @typescript-eslint/no-useless-constructor
});

// Mixin - symbol as emitteryPropertyName
Emittery.mixin(Symbol('emittery'))(MixinBase);

// Mixin - works with abstract class (validates `abstract new` constraint)
@Emittery.mixin('emittery')
abstract class MixinAbstractClass {
	abstract abstractMethod(): void;
}

// Mixin - as TC39 decorator
@Emittery.mixin('emittery')
class MixinDecoratorClass {
	test() {}
}

// Mixin - as TC39 decorator with specific method names
@Emittery.mixin('emittery', ['emit', 'on'])
class MixinDecoratorWithMethodNames {
	test() {}
}

// Mixin - error: non-string/symbol as emitteryPropertyName
expectError(Emittery.mixin(42));

// Mixin - error: string instead of array for methodNames
expectError(Emittery.mixin('emittery', 'on'));

// Mixin - error: plain object as target (not a constructor)
expectError(Emittery.mixin('emittery')({}));

// Symbol.dispose - UnsubscribeFunction is Disposable
{
	const ee = new Emittery();
	const off = ee.on('anEvent', () => {});
	expectAssignable<Disposable>(off);
	expectType<() => void>(off[Symbol.dispose]);

	const offAny = ee.onAny(() => {});
	expectAssignable<Disposable>(offAny);

	const offInit = ee.init('anEvent', () => {});
	expectAssignable<Disposable>(offInit);
}

// Symbol.asyncDispose - iterators are AsyncDisposable
{
	const ee = new Emittery();
	const eventsIterator = ee.events('anEvent');
	expectAssignable<AsyncDisposable>(eventsIterator);

	const anyIterator = ee.anyEvent();
	expectAssignable<AsyncDisposable>(anyIterator);
}

// Once with signal option
{
	const ee = new Emittery();
	ee.once('anEvent', {signal: new AbortController().signal});
	ee.once('anEvent', {predicate: () => true, signal: new AbortController().signal});
	ee.once('anEvent', {predicate: () => true});
}

// Events with signal option
{
	const ee = new Emittery();
	ee.events('anEvent', {signal: new AbortController().signal});
}

// AnyEvent with signal option
{
	const ee = new Emittery();
	ee.anyEvent({signal: new AbortController().signal});
}
```

## File: `license`
```
MIT License

Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (https://sindresorhus.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `maps.js`
```javascript
export const anyMap = new WeakMap();
export const eventsMap = new WeakMap();
export const producersMap = new WeakMap();
export const lifecycleMap = new WeakMap();
```

## File: `package.json`
```json
{
	"name": "emittery",
	"version": "2.0.0",
	"description": "Simple and modern async event emitter",
	"license": "MIT",
	"repository": "sindresorhus/emittery",
	"funding": "https://github.com/sindresorhus/emittery?sponsor=1",
	"author": {
		"name": "Sindre Sorhus",
		"email": "sindresorhus@gmail.com",
		"url": "https://sindresorhus.com"
	},
	"type": "module",
	"exports": {
		"types": "./index.d.ts",
		"default": "./index.js"
	},
	"sideEffects": false,
	"engines": {
		"node": ">=22"
	},
	"scripts": {
		"test": "xo && ava && tsd"
	},
	"files": [
		"index.js",
		"index.d.ts",
		"maps.js"
	],
	"keywords": [
		"event",
		"emitter",
		"eventemitter",
		"events",
		"async",
		"emit",
		"on",
		"once",
		"off",
		"listener",
		"subscribe",
		"unsubscribe",
		"pubsub",
		"tiny",
		"addlistener",
		"addeventlistener",
		"dispatch",
		"dispatcher",
		"observer",
		"trigger",
		"await",
		"promise",
		"typescript",
		"ts",
		"typed"
	],
	"devDependencies": {
		"@types/node": "^25.3.2",
		"ava": "^6.4.1",
		"delay": "^7.0.0",
		"p-event": "^7.1.0",
		"tsd": "^0.33.0",
		"xo": "^1.2.3"
	}
}
```

## File: `readme.md`
```markdown
# <img src="media/header.png" width="1000">

> Simple and modern async event emitter

<!-- [![Coverage Status](https://codecov.io/gh/sindresorhus/emittery/branch/main/graph/badge.svg)](https://codecov.io/gh/sindresorhus/emittery) -->
[![](https://badgen.net/bundlephobia/minzip/emittery)](https://bundlephobia.com/result?p=emittery)

It works in Node.js and the browser (using a bundler).

**Highlights**

- Async-first — listeners are deferred to the next microtask, keeping your code non-blocking
- TypeScript support with strongly typed events
- Async iteration and `for await...of` support
- [Lifecycle hooks](#initeventname-initfn) (`init`/`deinit`) for lazy resource setup and teardown
- [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) support for cancellation
- [`Symbol.dispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose) / [`Symbol.asyncDispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose) support for automatic cleanup
- [Meta events](#custom-subscribable-events) for observing listener changes
- [Debug mode](#debugging) with customizable logging
- Zero dependencies

Emitting events asynchronously is important for production code where you want the least amount of synchronous operations. Since JavaScript is single-threaded, no other code can run while doing synchronous operations. For Node.js, that means it will block other requests, defeating the strength of the platform, which is scalability through async. In the browser, a synchronous operation could potentially cause lags and block user interaction.

## Install

```sh
npm install emittery
```

## Usage

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', ({data}) => {
	console.log(data);
});

const myUnicorn = Symbol('🦄');

emitter.on(myUnicorn, ({data}) => {
	console.log(`Unicorns love ${data}`);
});

emitter.emit('🦄', '🌈'); // Will trigger printing '🌈'
emitter.emit(myUnicorn, '🦋');  // Will trigger printing 'Unicorns love 🦋'
```

## API

### eventName

Emittery accepts strings, symbols, and numbers as event names.

Symbol event names are preferred given that they can be used to avoid name collisions when your classes are extended, especially for internal events.

### isDebugEnabled

Toggle debug mode for all instances.

Default: `true` if the `DEBUG` environment variable is set to `emittery` or `*`, otherwise `false`.

Example:

```js
import Emittery from 'emittery';

Emittery.isDebugEnabled = true;

const emitter1 = new Emittery({debug: {name: 'myEmitter1'}});
const emitter2 = new Emittery({debug: {name: 'myEmitter2'}});

emitter1.on('test', () => {
	// …
});

emitter2.on('otherTest', () => {
	// …
});

emitter1.emit('test');
//=> [16:43:20.417][emittery:subscribe][myEmitter1] Event Name: test
//	data: undefined

emitter2.emit('otherTest');
//=> [16:43:20.417][emittery:subscribe][myEmitter2] Event Name: otherTest
//	data: undefined
```

### emitter = new Emittery(options?)

Create a new instance of Emittery.

#### options?

Type: `object`

Configure the new instance of Emittery.

##### debug?

Type: `object`

Configure the debugging options for this instance.

###### name

Type: `string`\
Default: `undefined`

Define a name for the instance of Emittery to use when outputting debug data.

Example:

```js
import Emittery from 'emittery';

Emittery.isDebugEnabled = true;

const emitter = new Emittery({debug: {name: 'myEmitter'}});

emitter.on('test', () => {
	// …
});

emitter.emit('test');
//=> [16:43:20.417][emittery:subscribe][myEmitter] Event Name: test
//	data: undefined
```

###### enabled?

Type: `boolean`\
Default: `false`

Toggle debug logging just for this instance.

Example:

```js
import Emittery from 'emittery';

const emitter1 = new Emittery({debug: {name: 'emitter1', enabled: true}});
const emitter2 = new Emittery({debug: {name: 'emitter2'}});

emitter1.on('test', () => {
	// …
});

emitter2.on('test', () => {
	// …
});

emitter1.emit('test');
//=> [16:43:20.417][emittery:subscribe][emitter1] Event Name: test
//	data: undefined

emitter2.emit('test');
```

###### logger?

Type: `Function(string, string, EventName?, Record<string, any>?) => void`

Default:

```js
(type, debugName, eventName, eventData) => {
	try {
		eventData = JSON.stringify(eventData);
	} catch {
		eventData = `Object with the following keys failed to stringify: ${Object.keys(eventData).join(',')}`;
	}

	if (typeof eventName === 'symbol' || typeof eventName === 'number') {
		eventName = eventName.toString();
	}

	const currentTime = new Date();
	const logTime = `${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}.${currentTime.getMilliseconds()}`;
	console.log(`[${logTime}][emittery:${type}][${debugName}] Event Name: ${eventName}\n\tdata: ${eventData}`);
}
```

Function that handles debug data.

Example:

```js
import Emittery from 'emittery';

const myLogger = (type, debugName, eventName, eventData) => {
	console.log(`[${type}]: ${eventName}`);
};

const emitter = new Emittery({
	debug: {
		name: 'myEmitter',
		enabled: true,
		logger: myLogger
	}
});

emitter.on('test', () => {
	// …
});

emitter.emit('test');
//=> [subscribe]: test
```

#### on(eventName | eventName[], listener, options?: {signal?: AbortSignal})

Subscribe to one or more events.

Returns an unsubscribe method (which is also [`Disposable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose), so it can be used with `using`).

Using the same listener multiple times for the same event will result in only one method call per emitted event.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', ({data}) => {
	console.log(data);
});

emitter.on(['🦄', '🐶'], ({name, data}) => {
	console.log(name, data);
});

emitter.emit('🦄', '🌈'); // log => '🌈' and '🦄 🌈'
emitter.emit('🐶', '🍖'); // log => '🐶 🍖'
```

You can pass an [abort signal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to unsubscribe too:

```js
import Emittery from 'emittery';

const emitter = new Emittery();
const abortController = new AbortController();

emitter.on('🐗', ({data}) => {
	console.log(data);
}, {signal: abortController.signal});

abortController.abort();
emitter.emit('🐗', '🍞'); // Nothing happens
```

Or use `using` for automatic cleanup when leaving scope:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

{
	using off = emitter.on('🦄', ({data}) => {
		console.log(data);
	});
	await emitter.emit('🦄', '🌈'); // Logs '🌈'
}

await emitter.emit('🦄', '🌈'); // Nothing happens
```

##### Custom subscribable events

Emittery exports some symbols which represent "meta" events that can be passed to `Emittery.on` and similar methods.

- `Emittery.listenerAdded` - Fires when an event listener was added.
- `Emittery.listenerRemoved` - Fires when an event listener was removed.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on(Emittery.listenerAdded, ({data: {listener, eventName}}) => {
	console.log(listener);
	//=> ({data}) => {}

	console.log(eventName);
	//=> '🦄'
});

emitter.on('🦄', ({data}) => {
	// Handle data
});
```

###### Listener data

- `listener` - The listener that was added.
- `eventName` - The name of the event that was added or removed if `.on()` or `.off()` was used, or `undefined` if `.onAny()` or `.offAny()` was used.

Only events that are not of this type are able to trigger these events.

##### listener({name, data?})

#### off(eventName | eventName[], listener)

Remove one or more event subscriptions.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

const listener = ({data}) => {
	console.log(data);
};

emitter.on(['🦄', '🐶', '🦊'], listener);
await emitter.emit('🦄', 'a');
await emitter.emit('🐶', 'b');
await emitter.emit('🦊', 'c');
emitter.off('🦄', listener);
emitter.off(['🐶', '🦊'], listener);
await emitter.emit('🦄', 'a'); // Nothing happens
await emitter.emit('🐶', 'b'); // Nothing happens
await emitter.emit('🦊', 'c'); // Nothing happens
```

##### listener({name, data?})

#### once(eventName | eventName[], predicateOrOptions?)

Subscribe to one or more events only once. It will be unsubscribed after the first event that matches the predicate (if provided).

The second argument can be a predicate function or an options object with `predicate` and/or `signal`.

Returns a promise for the event data when `eventName` is emitted and predicate matches (if provided). This promise is extended with an `off` method.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

const {data} = await emitter.once('🦄');
console.log(data);
//=> '🌈'
```

```js
// With multiple event names
const {name, data} = await emitter.once(['🦄', '🐶']);
console.log(name, data);
```

```js
// With predicate
const event = await emitter.once('data', ({data}) => data.ok === true);
console.log(event.data);
//=> {ok: true, value: 42}
```

You can pass an [abort signal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the subscription. If the signal is aborted before the event fires, the returned promise rejects with the signal's reason. This is useful for timeouts:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

// Reject if 'ready' doesn't fire within 5 seconds
await emitter.once('ready', {signal: AbortSignal.timeout(5000)});
```

The returned promise has an `off` method to cancel the subscription without rejecting:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

const promise = emitter.once('🦄');
// Cancel the subscription (the promise will never resolve)
promise.off();
```

#### events(eventName, options?: {signal?: AbortSignal})

Get an async iterator which buffers data each time an event is emitted.

Call `return()` on the iterator to remove the subscription. You can also pass an [abort signal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the subscription externally, or use `await using` for automatic cleanup.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

for await (const {data} of emitter.events('🦄')) {
	console.log(data);

	if (data === '🌈2') {
		break; // Revoke the subscription when we see the value '🌈2'.
	}
}
```

It accepts multiple event names:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

for await (const {name, data} of emitter.events(['🦄', '🦊'])) {
	console.log(name, data);
}
```

You can use `await using` for automatic cleanup when leaving scope:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

{
	await using iterator = emitter.events('🦄');
	for await (const {data} of iterator) {
		console.log(data);
	}
} // Subscription is automatically revoked
```

Since Emittery requires Node.js 22+, you can use the built-in [async iterator helpers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator#iterator_helpers) to transform events:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

for await (const {data} of emitter.events('🦄').filter(event => event.data > 3).take(5)) {
	console.log(data);
}
```

#### emit(eventName, data?)

Trigger an event asynchronously, optionally with some data. Listeners are called in the order they were added, but executed concurrently.

Returns a promise that resolves when all the event listeners are done. *Done* meaning executed if synchronous or resolved when an async/promise-returning function. You usually wouldn't want to wait for this, but you could for example catch possible errors. If any listeners throw/reject, the returned promise rejects with an `AggregateError` — all listener errors are collected in `error.errors`, so no errors are silently lost. All listeners always run to completion, even if some throw or reject.

#### emitSerial(eventName, data?)

Same as above, but it waits for each listener to resolve before triggering the next one. This can be useful if your events depend on each other. Although ideally they should not. Prefer `emit()` whenever possible.

If any of the listeners throw/reject, the returned promise will be rejected with the error and the remaining listeners will *not* be called.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', async () => {
	console.log('listener 1 start');
	await new Promise(resolve => setTimeout(resolve, 100));
	console.log('listener 1 done');
});

emitter.on('🦄', () => {
	console.log('listener 2'); // Only runs after listener 1 is done
});

await emitter.emitSerial('🦄');
```

#### onAny(listener, options?: {signal?: AbortSignal})

Subscribe to be notified about any event.

Returns a method to unsubscribe (which is also [`Disposable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)). Abort signal is respected too.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

const off = emitter.onAny(({name, data}) => {
	console.log(name, data);
});

emitter.emit('🦄', '🌈'); // log => '🦄 🌈'
emitter.emit('🐶', '🍖'); // log => '🐶 🍖'

off();
```

##### listener({name, data?})

#### offAny(listener)

Remove an `onAny` subscription.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

const listener = ({name, data}) => {
	console.log(name, data);
};

emitter.onAny(listener);
emitter.emit('🦄', '🌈'); // log => '🦄 🌈'
emitter.offAny(listener);
emitter.emit('🦄', '🌈'); // Nothing happens
```

#### anyEvent(options?: {signal?: AbortSignal})

Get an async iterator which buffers an event object each time an event is emitted.

Call `return()` on the iterator to remove the subscription. You can also pass an [abort signal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the subscription externally, or use `await using` for automatic cleanup.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

for await (const {name, data} of emitter.anyEvent()) {
	console.log(name, data);
}
```

You can use `await using` for automatic cleanup when leaving scope:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

{
	await using iterator = emitter.anyEvent();
	for await (const {name, data} of iterator) {
		console.log(name, data);
	}
} // Subscription is automatically revoked
```

#### clearListeners(eventNames?)

Clear all event listeners on the instance.

If `eventNames` is given, only the listeners for those events are cleared. Accepts a single event name or an array.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', listener);
emitter.on('🐶', listener);
emitter.on('🦊', listener);

// Clear a single event
emitter.clearListeners('🦄');

// Clear multiple events
emitter.clearListeners(['🐶', '🦊']);

// Clear all events
emitter.clearListeners();
```

#### init(eventName, initFn)

Register a function to be called when the first `.on()` listener subscribes to `eventName`. The `initFn` can optionally return a cleanup (deinit) function, which is called when the last `.on()` listener unsubscribes (or when `clearListeners()` removes all listeners for that event).

If `.on()` listeners already exist when `init()` is called, `initFn` is called immediately.

Returns an unsubscribe function (which is also [`Disposable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)). Calling it removes the init/deinit hooks, and if the init is currently active, it calls deinit immediately.

> [!NOTE]
> Lifecycle hooks only apply to `.on()` listeners. Subscriptions via `.events()` async iterators do not trigger the init or deinit functions.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.init('mouse', () => {
	terminal.grabInput({mouse: 'button'});

	terminal.on('mouse', (name, data) => {
		emitter.emit('mouse', data);
	});

	// Optional: return cleanup (deinit) function
	return () => {
		terminal.releaseInput();
	};
});

// Init is called when the first listener subscribes
const off = emitter.on('mouse', handler);

// Adding more listeners does not call init again
emitter.on('mouse', anotherHandler);

// Removing one listener does not call deinit yet
off();

// Deinit is called when the last listener unsubscribes
emitter.off('mouse', anotherHandler);
```

You can use `using` for automatic cleanup of the init/deinit hooks:

```js
import Emittery from 'emittery';

const emitter = new Emittery();

{
	using removeInit = emitter.init('mouse', () => {
		startListening();
		return () => stopListening();
	});
} // init/deinit hooks are automatically removed
```

#### listenerCount(eventNames?)

The number of listeners for the `eventNames` or all events if not specified.

```js
import Emittery from 'emittery';

const emitter = new Emittery();

emitter.on('🦄', listener);
emitter.on('🐶', listener);

emitter.listenerCount('🦄'); // 1
emitter.listenerCount(); // 2
```

#### bindMethods(target, methodNames?)

Bind the given `methodNames`, or all `Emittery` methods if `methodNames` is not defined, into the `target` object.

```js
import Emittery from 'emittery';

const object = {};

new Emittery().bindMethods(object);

object.emit('event');
```

## TypeScript

The default `Emittery` class has generic types that can be provided by TypeScript users to strongly type the list of events and the data passed to their event listeners.

```ts
import Emittery from 'emittery';

const emitter = new Emittery<
	// Pass `{[eventName]: undefined | <eventArg>}` as the first type argument for events that pass data to their listeners.
	// A value of `undefined` in this map means the event listeners should expect no data, and a type other than `undefined` means the listeners will receive one argument of that type.
	{
		open: string,
		close: undefined
	}
>();

// Typechecks just fine because the data type for the `open` event is `string`.
emitter.emit('open', 'foo\n');

// Typechecks just fine because `close` is present but points to undefined in the event data type map.
emitter.emit('close');

// TS compilation error because `1` isn't assignable to `string`.
emitter.emit('open', 1);

// TS compilation error because `other` isn't defined in the event data type map.
emitter.emit('other');
```

### Emittery.mixin(emitteryPropertyName, methodNames?)

A decorator which mixins `Emittery` as property `emitteryPropertyName` and `methodNames`, or all `Emittery` methods if `methodNames` is not defined, into the target class.

```ts
import Emittery from 'emittery';

@Emittery.mixin('emittery')
class MyClass {}

const instance = new MyClass();

instance.emit('event');
```

## Scheduling details

Listeners are not invoked for events emitted *before* the listener was added. Removing a listener will prevent that listener from being invoked, even if events are in the process of being (asynchronously!) emitted. This also applies to `.clearListeners()`, which removes all listeners. Listeners will be called in the order they were added. So-called *any* listeners are called *after* event-specific listeners.

Listeners always fire asynchronously — they are deferred to the next microtask, so any synchronous code after an unawaited `emit()` call runs first. If ordering matters, use `await emit()`.

Note that when using `.emitSerial()`, a slow listener will delay invocation of subsequent listeners. It's possible for newer events to overtake older ones.

## Debugging

Emittery can collect and log debug information.

To enable this feature set the DEBUG environment variable to `'emittery'` or `'*'`. Additionally you can set the static `isDebugEnabled` variable to true on the Emittery class, or `myEmitter.debug.enabled` on an instance of it for debugging a single instance.

See [API](#api) for more details on how debugging works.

## FAQ

### How is this different than the built-in `EventEmitter` in Node.js?

There are many things to not like about `EventEmitter`: its huge API surface, synchronous event emitting, magic error event, flawed memory leak detection. Emittery has none of that.

### Isn't `EventEmitter` synchronous for a reason?

Mostly backwards compatibility reasons. The Node.js team can't break the whole ecosystem.

It also allows silly code like this:

```js
let unicorn = false;

emitter.on('🦄', () => {
	unicorn = true;
});

emitter.emit('🦄');

console.log(unicorn);
//=> true
```

But I would argue doing that shows a deeper lack of Node.js and async comprehension and is not something we should optimize for. The benefit of async emitting is much greater.

### Can you support synchronous `emit()`?

No. Async emission is Emittery's core design principle. If you need synchronous event emission (for example, proxying DOM events like React's `onChange`), use a synchronous event emitter.

### Can you support multiple arguments for `emit()`?

No, just use [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment):

```js
emitter.on('🦄', ({data: [foo, bar]}) => {
	console.log(foo, bar);
});

emitter.emit('🦄', [foo, bar]);
```

## Related

- [p-event](https://github.com/sindresorhus/p-event) - Promisify an event by waiting for it to be emitted
```

## File: `examples/.gitignore`
```
/clocktyped.js
```

## File: `examples/clock.js`
```javascript
#!/usr/bin/env node
import process from 'node:process';
import Emittery from '../index.js';

class Clock extends Emittery {
	constructor() {
		super();
		this.startedAt = 0;
		this.timer = null;
	}

	tick() {
		if (!this.timer) {
			this.emit('error', new Error('Clock has not been started'));
			return;
		}

		const now = Date.now();
		const duration = now - this.startedAt;

		this.emit('tick', {duration, now});
	}

	start() {
		if (this.timer) {
			throw new Error('Clock has already been started');
		}

		this.startedAt = Date.now();
		this.timer = setInterval(this.tick.bind(this), 1000);

		this.emit('start');
	}

	stop() {
		if (this.timer) {
			clearInterval(this.timer);
		}

		this.startedAt = 0;
		this.timer = null;

		this.emit('stop');
	}
}

function onTick({duration}) {
	console.log(Math.floor(duration / 1000));

	if (duration >= 6000) {
		stop();
	}
}

function onError(error) {
	process.exitCode = 1;
	console.error(error);
	stop();
}

const timer = new Clock();
const offTick = timer.on('tick', onTick);
const offError = timer.on('error', onError);

function stop() {
	offTick();
	offError();
	timer.stop();
}

timer.start();
// Prints:
// 		1
// 		2
// 		3
// 		4
// 		5
// 		6
```

## File: `examples/clocktyped.ts`
```typescript
#!/usr/bin/env npx ts-node
/* eslint-disable @typescript-eslint/no-floating-promises */
import process from 'node:process';
import {setInterval} from 'node:timers';
import Emittery from '../index.js';

type TickData = {
	now: number;
	duration: number;
};

// Map Clock's events emitting data to the type of their data.
type EventDataMap = {
	tick: TickData;
	error: Error;
	start: undefined;
	stop: undefined;
};

class Clock extends Emittery<EventDataMap> {
	private startedAt = 0;
	private timer: ReturnType<typeof setInterval> | undefined;

	public constructor() {
		super();
	}

	public start() {
		if (this.timer) {
			throw new Error('Clock has already been started');
		}

		this.startedAt = Date.now();
		this.timer = setInterval(this.tick.bind(this), 1000);

		this.emit('start');
	}

	public stop() {
		if (this.timer) {
			clearInterval(this.timer);
		}

		this.startedAt = 0;
		this.timer = undefined;

		this.emit('stop');
	}

	private tick() {
		if (!this.timer) {
			this.emit('error', new Error('Clock has not been started'));
			return;
		}

		const now = Date.now();
		const duration = now - this.startedAt;

		this.emit('tick', {duration, now});
	}
}

function onTick({duration}: TickData) {
	console.log(Math.floor(duration / 1000));

	if (duration >= 6000) {
		stop();
	}
}

function onError(error: Error) {
	process.exitCode = 1;
	console.error(error);
	stop();
}

const timer = new Clock();
const offTick = timer.on('tick', onTick);
const offError = timer.on('error', onError);

function stop() {
	offTick();
	offError();
	timer.stop();
}

timer.start();
// Prints:
// 		1
// 		2
// 		3
// 		4
// 		5
// 		6
```

## File: `examples/emit.js`
```javascript
#!/usr/bin/env node
import Emittery from '../index.js';

const myEmitter = new Emittery();

// Register listener
myEmitter.on('event', () => {
	console.log('an event occurred!');
});

myEmitter.onAny(eventName => {
	console.log('`%s` event occurred!', eventName);
});

// Emit event in next tick
myEmitter.emit('event');

// Prints:
// 		an event occurred!
// 		`event` event occurred!
```

## File: `examples/emitonce.js`
```javascript
#!/usr/bin/env node
import Emittery from '../index.js';

const myEmitter = new Emittery();

// Register listener for only the one event
(async () => { // eslint-disable-line unicorn/prefer-top-level-await
	console.log('An event occurred (#%d).', await myEmitter.once('event'));
})();

// Emit events in next tick
myEmitter.emit('event', 1);
myEmitter.emit('event', 2);

// Prints:
//		An event occurred (#1).
```

## File: `examples/eventdata.js`
```javascript
#!/usr/bin/env node
import Emittery from '../index.js';

const myEmitter = new Emittery();

// Does not provide a context either.
myEmitter.on('event', function ({a, b}, ...arguments_) {
	console.log(a, b, arguments_, this);
});

// Only accept one event data parameter
myEmitter.emit('event', {a: true, b: true}, 'not', 'supported');

// Prints:
// 		true true [] undefined
```

## File: `test/index.js`
```javascript
import test from 'ava';
import delay from 'delay';
import {pEvent, pEventMultiple} from 'p-event';
import Emittery from '../index.js';
import {eventsMap} from '../maps.js';

test('on()', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('eventName');
	const calls = [];
	const listener1 = () => {
		calls.push(1);
	};

	const listener2 = () => {
		calls.push(2);
	};

	const listener3 = () => {
		calls.push(3);
	};

	emitter.on('🦄', listener1);
	emitter.on('🦄', listener2);
	emitter.on(eventName, listener3);
	await emitter.emit('🦄');
	await emitter.emit(eventName);
	t.deepEqual(calls, [1, 2, 3]);
});

test('on() - multiple event names', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('eventName');
	let count = 0;
	const listener = () => {
		++count;
	};

	emitter.on(['🦄', '🐶', eventName], listener);
	await emitter.emit('🦄');
	await emitter.emit('🐶');
	await emitter.emit(eventName);
	t.is(count, 3);
});

test('on() - symbol eventName', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('eventName');
	const calls = [];
	const listener1 = () => {
		calls.push(1);
	};

	const listener2 = () => {
		calls.push(2);
	};

	emitter.on(eventName, listener1);
	emitter.on(eventName, listener2);
	await emitter.emit(eventName);
	t.deepEqual(calls, [1, 2]);
});

test('on() - listenerAdded', async t => {
	const emitter = new Emittery();
	const addListener = () => 1;
	setImmediate(() => emitter.on('abc', addListener));
	const {data: {eventName, listener}} = await pEvent(emitter, Emittery.listenerAdded, {
		rejectionEvents: [],
	});
	t.is(listener, addListener);
	t.is(eventName, 'abc');
});

test('on() - listenerRemoved', async t => {
	const emitter = new Emittery();
	const addListener = () => 1;
	emitter.on('abc', addListener);
	setImmediate(() => emitter.off('abc', addListener));
	const {data: {eventName, listener}} = await pEvent(emitter, Emittery.listenerRemoved, {
		rejectionEvents: [],
	});
	t.is(listener, addListener);
	t.is(eventName, 'abc');
});

test('on() - listenerAdded onAny', async t => {
	const emitter = new Emittery();
	const addListener = () => 1;
	setImmediate(() => emitter.onAny(addListener));
	const {data: {eventName, listener}} = await pEvent(emitter, Emittery.listenerAdded, {
		rejectionEvents: [],
	});
	t.is(listener, addListener);
	t.is(eventName, undefined);
});

test('off() - listenerAdded', t => {
	const emitter = new Emittery();
	const off = emitter.on(Emittery.listenerAdded, () => t.fail());
	off();
	emitter.emit('a');
	t.pass();
});

test('off() - isDebug logs output', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	const off = emitter.on('test', () => {});
	off();
	t.is(eventStore.length, 2);
	t.is(eventStore[1].type, 'unsubscribe');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
});

test('on() - listenerAdded offAny', async t => {
	const emitter = new Emittery();
	const addListener = () => 1;
	emitter.onAny(addListener);
	setImmediate(() => emitter.offAny(addListener));
	const {data: {listener, eventName}} = await pEvent(emitter, Emittery.listenerRemoved);
	t.is(listener, addListener);
	t.is(eventName, undefined);
});

test('meta event - works with async emit override in subclass', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerAdded, event => {
		events.push(event);
	});

	const listener = () => {};
	emitter.on('test', listener);

	await delay(50);
	t.is(events.length, 1);
	t.is(events[0].data.eventName, 'test');
	t.is(events[0].data.listener, listener);
});

test('meta event - works when emit override clones meta event data before forwarding', async t => {
	class CustomEmittery extends Emittery {
		emit(eventName, eventData) {
			if (eventName === Emittery.listenerAdded && eventData && typeof eventData === 'object') {
				return super.emit(eventName, {...eventData});
			}

			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerAdded, event => {
		events.push(event);
	});

	const listener = () => {};
	emitter.on('test', listener);

	await Promise.resolve();

	t.is(events.length, 1);
	t.is(events[0].data.eventName, 'test');
	t.is(events[0].data.listener, listener);
});

test('meta event - userland meta emit is blocked during debug logger reentrancy', async t => {
	let forgedMetaEmitPromise;

	const emitter = new Emittery({
		debug: {
			enabled: true,
			logger(type) {
				if (type === 'emit' && !forgedMetaEmitPromise) {
					forgedMetaEmitPromise = emitter.emit(Emittery.listenerAdded, {eventName: 'forged', listener() {}});
				}
			},
			name: 'testEmitter',
		},
	});

	const events = [];
	emitter.on(Emittery.listenerAdded, event => {
		events.push(event);
	});

	emitter.on('test', () => {});
	await emitter.emit('test');

	await t.throwsAsync(forgedMetaEmitPromise, {instanceOf: TypeError});
	await Promise.resolve();

	t.is(events.length, 1);
	t.is(events[0].data.eventName, 'test');
});

test('debug - on() does not log meta events', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'x',
			enabled: true,
			logger(type, _, eventName) {
				eventStore.push({type, eventName});
			},
		},
	});

	emitter.on('test', () => {});
	t.is(eventStore.length, 1);
	t.is(eventStore[0].type, 'subscribe');
	t.is(eventStore[0].eventName, 'test');
});

test('debug - off() does not log meta events', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'x',
			enabled: true,
			logger(type, _, eventName) {
				eventStore.push({type, eventName});
			},
		},
	});

	const off = emitter.on('test', () => {});
	off();
	// Subscribe + unsubscribe only; no listenerAdded/listenerRemoved meta event logs
	t.is(eventStore.length, 2);
	t.is(eventStore[0].type, 'subscribe');
	t.is(eventStore[1].type, 'unsubscribe');
});

test('debug - onAny() does not log meta events', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'x',
			enabled: true,
			logger(type, _, eventName) {
				eventStore.push({type, eventName});
			},
		},
	});

	emitter.onAny(() => {});
	t.is(eventStore.length, 1);
	t.is(eventStore[0].type, 'subscribeAny');
	t.is(eventStore[0].eventName, undefined);
});

test('debug - offAny() does not log meta events', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'x',
			enabled: true,
			logger(type, _, eventName) {
				eventStore.push({type, eventName});
			},
		},
	});

	const off = emitter.onAny(() => {});
	off();
	// SubscribeAny + unsubscribeAny only; no listenerAdded/listenerRemoved meta event logs
	t.is(eventStore.length, 2);
	t.is(eventStore[0].type, 'subscribeAny');
	t.is(eventStore[1].type, 'unsubscribeAny');
});

test.serial('meta event - internal emit does not attach catch handler', t => {
	const originalEmit = Emittery.prototype.emit;
	const emitter = new Emittery();
	let catchCalled = false;

	Emittery.prototype.emit = function (eventName, eventData) {
		if (eventName === Emittery.listenerAdded) {
			return {
				catch() {
					catchCalled = true;
				},
			};
		}

		return originalEmit.call(this, eventName, eventData);
	};

	try {
		emitter.on('test', () => {});
		t.false(catchCalled);
	} finally {
		Emittery.prototype.emit = originalEmit;
	}
});

test('meta event - userland remains blocked with async emit override present', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const listener = () => {};
	emitter.on('test', listener);

	await delay(50);

	await t.throwsAsync(emitter.emit(Emittery.listenerAdded), {instanceOf: TypeError});
	await t.throwsAsync(emitter.emit(Emittery.listenerRemoved), {instanceOf: TypeError});
});

test('meta event - userland cannot emit reserved events while internal meta emit is pending', async t => {
	const emitter = new Emittery();
	emitter.on('test', () => {});

	await t.throwsAsync(emitter.emit(Emittery.listenerAdded), {instanceOf: TypeError});
});

test('meta event - userland emit is blocked even when override delays meta event', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			if (eventName === Emittery.listenerAdded) {
				await delay(50);
			}

			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	emitter.on('test', () => {});

	await t.throwsAsync(Emittery.prototype.emit.call(emitter, Emittery.listenerAdded, {eventName: 'fake', listener() {}}), {instanceOf: TypeError});
});

test('meta event - rejected thenable override does not open meta emits', async t => {
	class CustomEmittery extends Emittery {
		emit(eventName, eventData) {
			if (eventName === Emittery.listenerAdded) {
				(async () => {
					try {
						await super.emit(eventName, eventData);
					} catch {}
				})();

				/* eslint-disable unicorn/no-thenable */
				return {
					then(_resolve, reject) {
						reject(new Error('thenable rejection'));
					},
				};
				/* eslint-enable unicorn/no-thenable */
			}

			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	t.notThrows(() => {
		emitter.on('test', () => {});
	});

	await Promise.resolve();

	await t.throwsAsync(Emittery.prototype.emit.call(emitter, Emittery.listenerRemoved, {eventName: 'fake', listener() {}}), {instanceOf: TypeError});
});

test('meta event - sync throw in emit override does not open meta emits', async t => {
	class CustomEmittery extends Emittery {
		emit(eventName, eventData) {
			if (eventName === Emittery.listenerAdded) {
				throw new Error('sync override error');
			}

			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();

	t.notThrows(() => {
		emitter.on('test', () => {});
	});

	await t.throwsAsync(emitter.emit(Emittery.listenerRemoved), {instanceOf: TypeError});
});

test('meta event - ignores non-promise finally method from emit override return value', async t => {
	class CustomEmittery extends Emittery {
		emit(eventName, eventData) {
			if (eventName === Emittery.listenerAdded) {
				return {
					finally(callback) {
						callback();
						throw new Error('throwing finally');
					},
				};
			}

			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();

	t.notThrows(() => {
		emitter.on('test', () => {});
	});

	await Promise.resolve();

	await t.throwsAsync(emitter.emit(Emittery.listenerRemoved), {instanceOf: TypeError});
});

test('meta event - listenerRemoved works with async emit override in subclass', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerRemoved, event => {
		events.push(event);
	});

	const listener = () => {};
	emitter.on('test', listener);
	emitter.off('test', listener);

	await delay(50);
	t.is(events.length, 1);
	t.is(events[0].data.eventName, 'test');
	t.is(events[0].data.listener, listener);
});

test('meta event - concurrent on() calls with async emit override both deliver', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerAdded, event => {
		events.push(event);
	});

	const listener1 = () => {};
	const listener2 = () => {};
	emitter.on('test', listener1);
	emitter.on('test', listener2);

	await delay(50);
	t.is(events.length, 2);

	const reportedListeners = new Set(events.map(event => event.data.listener));
	t.true(reportedListeners.has(listener1));
	t.true(reportedListeners.has(listener2));

	await t.throwsAsync(emitter.emit(Emittery.listenerAdded), {instanceOf: TypeError});
});

test('meta event - onAny() works with async emit override in subclass', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerAdded, event => {
		events.push(event);
	});

	const listener = () => {};
	emitter.onAny(listener);

	await delay(50);
	t.is(events.length, 1);
	t.is(events[0].data.eventName, undefined);
	t.is(events[0].data.listener, listener);
});

test('meta event - offAny() works with async emit override in subclass', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const events = [];
	emitter.on(Emittery.listenerRemoved, event => {
		events.push(event);
	});

	const listener = () => {};
	emitter.onAny(listener);
	emitter.offAny(listener);

	await delay(50);
	t.is(events.length, 1);
	t.is(events[0].data.eventName, undefined);
	t.is(events[0].data.listener, listener);
});

test('meta event - multiple emitters have independent counters', async t => {
	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			await delay(10);
			return super.emit(eventName, eventData);
		}
	}

	const emitter1 = new CustomEmittery();
	const emitter2 = new CustomEmittery();
	const events1 = [];
	const events2 = [];

	emitter1.on(Emittery.listenerAdded, event => {
		events1.push(event);
	});
	emitter2.on(Emittery.listenerAdded, event => {
		events2.push(event);
	});

	const listener = () => {};
	emitter1.on('test', listener);
	emitter2.on('test', listener);

	await delay(50);
	t.is(events1.length, 1);
	t.is(events2.length, 1);
	t.is(events1[0].data.listener, listener);
	t.is(events2[0].data.listener, listener);

	// Both counters settle independently - userland is blocked on both
	await t.throwsAsync(emitter1.emit(Emittery.listenerAdded), {instanceOf: TypeError});
	await t.throwsAsync(emitter2.emit(Emittery.listenerAdded), {instanceOf: TypeError});
});

test('on() - eventName must be a string, symbol, or number', t => {
	const emitter = new Emittery();

	emitter.on('string', () => {});
	emitter.on(Symbol('symbol'), () => {});
	emitter.on(42, () => {});

	t.throws(() => {
		emitter.on(true, () => {});
	}, {instanceOf: TypeError});
});

test('on() - must have a listener', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.on('🦄');
	}, {instanceOf: TypeError});
});

test('on() - returns an unsubscribe method', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	const off = emitter.on('🦄', listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	off();
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('on() - calling off() twice is a safe no-op', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	const off = emitter.on('🦄', listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	off();
	off();
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('on() - dedupes identical listeners', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	emitter.on('🦄', listener);
	emitter.on('🦄', listener);
	emitter.on('🦄', listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('on() - isDebug logs output', t => {
	const eventStore = [];
	const calls = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.on('test', data => calls.push(data));
	t.is(eventStore.length, 1);
	t.is(eventStore[0].type, 'subscribe');
	t.is(eventStore[0].debugName, 'testEmitter');
	t.is(eventStore[0].eventName, 'test');
});

test('on() - listener receives event object with eventName and data', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	emitter.emit('🦄', '🌈');
	t.deepEqual(await promise, {name: '🦄', data: '🌈'});
});

test('on() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	emitter.emit('🦄');
	const event = await promise;
	t.deepEqual(event, {name: '🦄'});
	t.false('data' in event);
});

test('on() - explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	emitter.emit('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('on() - listeners get isolated event objects', async t => {
	const emitter = new Emittery();
	let secondListenerEvent;

	emitter.on('🦄', event => {
		event.name = 'changed';
		event.data = 'changed';
	});

	emitter.on('🦄', event => {
		secondListenerEvent = event;
	});

	await emitter.emit('🦄', '🌈');
	t.deepEqual(secondListenerEvent, {name: '🦄', data: '🌈'});
});

test('on() - symbol eventName is included in event object', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('test');
	const promise = new Promise(resolve => {
		emitter.on(eventName, event => resolve(event));
	});
	emitter.emit(eventName, 'test data');
	t.deepEqual(await promise, {name: eventName, data: 'test data'});
});

test('on() - number eventName is included in event object', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on(42, event => resolve(event));
	});
	emitter.emit(42, 'data');
	t.deepEqual(await promise, {name: 42, data: 'data'});
});

test('on() - use abort signal', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	emitter.on('abc', listener, {signal: abortController.signal});

	await emitter.emit('abc');
	t.deepEqual(calls, [1]);

	abortController.abort();
	await emitter.emit('abc');

	t.deepEqual(calls, [1]);
});

test('on() - pre-aborted signal', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.on('🦄', () => {
		calls.push(1);
	}, {signal: AbortSignal.abort()});

	await emitter.emit('🦄');
	t.deepEqual(calls, []);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('on() - off() removes signal listener even if deinit throws', t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const {signal} = abortController;
	let abortListenerCount = 0;
	const addEventListener = signal.addEventListener.bind(signal);
	const removeEventListener = signal.removeEventListener.bind(signal);

	signal.addEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			++abortListenerCount;
		}

		addEventListener(eventName, listener, options);
	};

	signal.removeEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			--abortListenerCount;
		}

		removeEventListener(eventName, listener, options);
	};

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	const off = emitter.on('🦄', () => {}, {signal});
	t.is(abortListenerCount, 1);
	t.throws(() => {
		off();
	}, {message: 'deinit boom'});
	t.is(abortListenerCount, 0);
});

test('on() - abort signal ignores deinit throw', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	emitter.on('🦄', () => {}, {signal: abortController.signal});
	abortController.abort();

	await delay(0);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('on() - abort signal fully unsubscribes multiple event names when one deinit throws', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const calls = [];

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	emitter.init('🌈', () => () => {});

	emitter.on(['🦄', '🌈'], ({name}) => {
		calls.push(name);
	}, {signal: abortController.signal});

	abortController.abort();
	await delay(0);

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
	await emitter.emit('🌈');
	t.deepEqual(calls, []);
});

test.serial('events()', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');

	await emitter.emit('🦄', '🌈');
	setTimeout(() => {
		emitter.emit('🦄', Promise.resolve('🌟'));
	}, 10);

	t.plan(3);
	const expected = [
		{name: '🦄', data: '🌈'},
		{name: '🦄', data: '🌟'},
	];
	for await (const event of iterator) {
		t.deepEqual(event, expected.shift());
		if (expected.length === 0) {
			break;
		}
	}

	t.deepEqual(await iterator.next(), {done: true});
});

test.serial('events() - multiple event names', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events(['🦄', '🐶']);

	await emitter.emit('🦄', '🌈');
	await emitter.emit('🐶', '🌈');
	setTimeout(() => {
		emitter.emit('🦄', Promise.resolve('🌟'));
	}, 10);

	t.plan(4);
	const expected = [
		{name: '🦄', data: '🌈'},
		{name: '🐶', data: '🌈'},
		{name: '🦄', data: '🌟'},
	];
	for await (const event of iterator) {
		t.deepEqual(event, expected.shift());
		if (expected.length === 0) {
			break;
		}
	}

	t.deepEqual(await iterator.next(), {done: true});
});

test('events() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	await emitter.emit('🦄');
	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄'}});
	t.false('data' in result.value);
	await iterator.return();
});

test('events() - explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	await emitter.emit('🦄', undefined);
	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄', data: undefined}});
	t.true('data' in result.value);
	await iterator.return();
});

test('events() - symbol eventName is included in event object', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('test');
	const iterator = emitter.events(eventName);
	await emitter.emit(eventName, '🌈');
	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: eventName, data: '🌈'}});
	await iterator.return();
});

test('events() - iterators get isolated event objects', async t => {
	const emitter = new Emittery();
	const firstIterator = emitter.events('🦄');
	const secondIterator = emitter.events('🦄');

	await emitter.emit('🦄', '🌈');
	const first = await firstIterator.next();
	first.value.name = 'changed';
	first.value.data = 'changed';

	const second = await secondIterator.next();
	t.deepEqual(second, {done: false, value: {name: '🦄', data: '🌈'}});

	await firstIterator.return();
	await secondIterator.return();
});

test('events() - return() called during emit', async t => {
	const emitter = new Emittery();
	let iterator = null;
	emitter.on('🦄', () => {
		iterator.return();
	});
	iterator = emitter.events('🦄');
	emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});
	t.deepEqual(await iterator.next(), {done: true});
});

test('events() - return() awaits its argument', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	t.deepEqual(await iterator.return(Promise.resolve(1)), {done: true, value: 1});
});

test('events() - return() without argument', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	t.deepEqual(await iterator.return(), {done: true});
});

test('events() - discarded iterators should stop receiving events', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {value: {name: '🦄', data: '🌈'}, done: false});
	await iterator.return();
	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: true});

	setTimeout(() => {
		emitter.emit('🦄', '🌟');
	}, 10);

	await new Promise(resolve => {
		setTimeout(resolve, 20);
	});

	t.deepEqual(await iterator.next(), {done: true});
});

test('off()', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	emitter.on('🦄', listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	emitter.off('🦄', listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('off() - multiple event names', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	emitter.on(['🦄', '🐶', '🦊'], listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	emitter.off(['🦄', '🐶'], listener);
	await emitter.emit('🦄');
	await emitter.emit('🐶');
	t.deepEqual(calls, [1]);

	await emitter.emit('🦊');
	t.deepEqual(calls, [1, 1]);
});

test('off() - eventName must be a string, symbol, or number', t => {
	const emitter = new Emittery();

	emitter.on('string', () => {});
	emitter.on(Symbol('symbol'), () => {});
	emitter.on(42, () => {});

	t.throws(() => {
		emitter.off(true);
	}, {instanceOf: TypeError});
});

test('off() - no listener', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.off('🦄');
	}, {instanceOf: TypeError});
});

test('off() - clears global maps when all listeners are removed', t => {
	const emitter = new Emittery();

	const event = 'string';
	const callback = () => {};

	emitter.on(event, callback);
	t.is(eventsMap.get(emitter).get(event).size, 1);

	emitter.off(event, callback);
	t.is(eventsMap.get(emitter).get(event), undefined);
});

test('once()', async t => {
	const fixture = '🌈';
	const emitter = new Emittery();
	const promise = emitter.once('🦄');
	emitter.emit('🦄', fixture);
	t.deepEqual(await promise, {name: '🦄', data: fixture});
});

test('once() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const promise = emitter.once('🦄');
	emitter.emit('🦄');
	const event = await promise;
	t.deepEqual(event, {name: '🦄'});
	t.false('data' in event);
});

test('once() - explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = emitter.once('🦄');
	emitter.emit('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('once() - emitSerial explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = emitter.once('🦄');
	await emitter.emitSerial('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('once() - symbol eventName is included in event object', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('test');
	const promise = emitter.once(eventName);
	emitter.emit(eventName, '🌈');
	t.deepEqual(await promise, {name: eventName, data: '🌈'});
});

test('once() - multiple event names', async t => {
	const fixture = '🌈';
	const emitter = new Emittery();
	const promise = emitter.once(['🦄', '🐶']);
	emitter.emit('🐶', fixture);
	t.deepEqual(await promise, {name: '🐶', data: fixture});
});

test('once() - eventName must be a string, symbol, or number', async t => {
	const emitter = new Emittery();

	emitter.once('string');
	emitter.once(Symbol('symbol'));
	emitter.once(42);

	await t.throwsAsync(emitter.once(true), {instanceOf: TypeError});
});

test('once() - returns a promise with an unsubscribe method', async t => {
	const fixture = '🌈';
	const emitter = new Emittery();
	const oncePromise = emitter.once('🦄');

	const testFailurePromise = Promise.race([
		(async () => {
			await oncePromise;
			t.fail();
		})(),
		new Promise(resolve => {
			setTimeout(() => {
				resolve(false);
			}, 100);
		}),
	]);

	oncePromise.off();
	emitter.emit('🦄', fixture);

	await testFailurePromise;
	t.pass();
});

test('once() - supports filter predicate', async t => {
	const emitter = new Emittery();

	const oncePromise = emitter.once('data', ({data}) => data.ok === true);
	await emitter.emit('data', {ok: false, foo: 'bar'});

	const payload = {ok: true, value: 42};

	await emitter.emit('data', payload);
	await emitter.emit('data', {ok: true, other: 'value'});

	t.deepEqual(await oncePromise, {name: 'data', data: payload});
});

test('once() - filter predicate receives full event object with eventName', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('test');
	const oncePromise = emitter.once(eventName, event => event.name === eventName && event.data === 'match');
	await emitter.emit(eventName, 'no match');
	await emitter.emit(eventName, 'match');
	t.deepEqual(await oncePromise, {name: eventName, data: 'match'});
});

test('once() - filter predicate must be a function', async t => {
	const emitter = new Emittery();
	await t.throwsAsync(
		emitter.once('data', 'not a function'),
		{
			instanceOf: TypeError,
			message: 'predicate must be a function',
		},
	);
});

test('once() - filter predicate with multiple event names', async t => {
	const emitter = new Emittery();
	const payload = {ok: true, value: 42};

	const oncePromise = emitter.once(['data1', 'data2'], ({data}) => data.ok === true);
	await emitter.emit('data1', {ok: false});
	await emitter.emit('data2', payload);

	t.deepEqual(await oncePromise, {name: 'data2', data: payload});
});

test('once() - filter predicate can be unsubscribed', async t => {
	const emitter = new Emittery();
	const oncePromise = emitter.once('data', ({data}) => data.ok === true);

	oncePromise.off();
	await emitter.emit('data', {ok: true});

	const testPromise = Promise.race([
		oncePromise,
		new Promise(resolve => {
			setTimeout(() => resolve('timeout'), 100);
		}),
	]);

	t.is(await testPromise, 'timeout');
});

test('once() - supports filter predicate as options object', async t => {
	const emitter = new Emittery();

	const oncePromise = emitter.once('data', {predicate: ({data}) => data.ok === true});
	await emitter.emit('data', {ok: false, foo: 'bar'});

	const payload = {ok: true, value: 42};

	await emitter.emit('data', payload);

	t.deepEqual(await oncePromise, {name: 'data', data: payload});
});

test('emitSerial() - listener receives event object with eventName and data', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	await emitter.emitSerial('🦄', '🌈');
	t.deepEqual(await promise, {name: '🦄', data: '🌈'});
});

test('emitSerial() - explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	await emitter.emitSerial('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('emitSerial() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.on('🦄', event => resolve(event));
	});
	await emitter.emitSerial('🦄');
	const event = await promise;
	t.deepEqual(event, {name: '🦄'});
	t.false('data' in event);
});

test('emit() - one event', async t => {
	const emitter = new Emittery();
	const eventFixture = {foo: true};
	const promise = pEvent(emitter, '🦄');
	emitter.emit('🦄', eventFixture);
	t.deepEqual(await promise, {name: '🦄', data: eventFixture});
});

test('emit() - multiple events', async t => {
	const emitter = new Emittery();
	const expectedCount = 5;

	emitter.on('🦄', async () => {
		await delay(Math.random() * 100);
	});

	const promise = pEventMultiple(emitter, '🦄', {count: expectedCount});

	emitter.emit('🦄');
	emitter.emit('🦄');
	emitter.emit('🦄');
	emitter.emit('🦄');
	emitter.emit('🦄');

	const result = await promise;

	t.is(result.length, expectedCount);
});

test('emit() - eventName must be a string, symbol, or number', async t => {
	const emitter = new Emittery();

	emitter.emit('string');
	emitter.emit(Symbol('symbol'));
	emitter.emit(42);

	await t.throwsAsync(emitter.emit(true), {instanceOf: TypeError});
});

test('emit() - userland cannot emit the meta events', async t => {
	const emitter = new Emittery();

	await t.throwsAsync(emitter.emit(Emittery.listenerRemoved), {instanceOf: TypeError});
	await t.throwsAsync(emitter.emit(Emittery.listenerAdded), {instanceOf: TypeError});
});

test('emit() - is async', async t => {
	const emitter = new Emittery();
	const promise = pEvent(emitter, '🦄');

	let unicorn = false;
	emitter.on('🦄', () => {
		unicorn = true;
	});

	emitter.emit('🦄');

	t.false(unicorn);

	await promise;

	t.true(unicorn);
});

test('emit() - unawaited emits fire after synchronous code (by design)', async t => {
	const emitter = new Emittery();
	const log = [];

	emitter.on('unicorn', () => {
		log.push('listener');
	});

	const p1 = emitter.emit('unicorn');
	log.push('after emit 1');
	const p2 = emitter.emit('unicorn');
	log.push('after emit 2');

	await Promise.all([p1, p2]);

	// Listeners fire after all synchronous code because emit() yields to the microtask queue
	t.deepEqual(log, ['after emit 1', 'after emit 2', 'listener', 'listener']);
});

test('emit() - awaits async listeners', async t => {
	const emitter = new Emittery();
	let unicorn = false;

	emitter.on('🦄', async () => {
		await Promise.resolve();
		unicorn = true;
	});

	const promise = emitter.emit('🦄');
	t.false(unicorn);
	await promise;
	t.true(unicorn);
});

test('emit() - calls listeners subscribed when emit() was invoked', async t => {
	const emitter = new Emittery();
	const calls = [];
	const off1 = emitter.on('🦄', () => {
		calls.push(1);
	});
	const p = emitter.emit('🦄');
	emitter.on('🦄', () => {
		calls.push(2);
	});
	await p;
	t.deepEqual(calls, [1]);

	const off3 = emitter.on('🦄', () => {
		calls.push(3);
		off1();
		emitter.on('🦄', () => {
			calls.push(4);
		});
	});
	await emitter.emit('🦄');
	t.deepEqual(calls, [1, 1, 2, 3]);
	off3();

	const off5 = emitter.on('🦄', () => {
		calls.push(5);
		emitter.onAny(() => {
			calls.push(6);
		});
	});
	await emitter.emit('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5]);
	off5();

	let off8 = null;
	emitter.on('🦄', () => {
		calls.push(7);
		off8();
	});
	off8 = emitter.on('🦄', () => {
		calls.push(8);
	});
	await emitter.emit('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6]);

	let off10 = null;
	emitter.onAny(() => {
		calls.push(9);
		off10();
	});
	off10 = emitter.onAny(() => {
		calls.push(10);
	});
	await emitter.emit('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9]);

	await emitter.emit('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9, 2, 4, 7, 6, 9]);

	const p2 = emitter.emit('🦄');
	emitter.clearListeners();
	await p2;
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9, 2, 4, 7, 6, 9]);
});

test('emit() - isDebug logs output', async t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.on('test', () => {});
	await emitter.emit('test', 'data');
	t.is(eventStore.length, 2);
	t.is(eventStore[1].type, 'emit');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
	t.is(eventStore[1].eventData, 'data');
});

test('emit() - returns undefined', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => '🌈');
	t.is(await emitter.emit('🦄'), undefined);

	emitter.on('🦄🦄', async () => '🌈');
	t.is(await emitter.emit('🦄🦄'), undefined);
});

test('emit() - throws an AggregateError if any listener throws', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => {
		throw new Error('🌈');
	});
	const error = await t.throwsAsync(emitter.emit('🦄'), {instanceOf: AggregateError});
	t.is(error.errors.length, 1);
	t.is(error.errors[0].message, '🌈');

	const emitter2 = new Emittery();
	emitter2.on('🦄🦄', async () => {
		throw new Error('🌈');
	});
	const error2 = await t.throwsAsync(emitter2.emit('🦄🦄'), {instanceOf: AggregateError});
	t.is(error2.errors.length, 1);
	t.is(error2.errors[0].message, '🌈');
});

test('emit() - collects all listener errors into AggregateError', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => {
		throw new Error('first');
	});
	emitter.on('🦄', () => {
		throw new Error('second');
	});

	const error = await t.throwsAsync(emitter.emit('🦄'), {instanceOf: AggregateError});
	t.is(error.errors.length, 2);
	const messages = new Set(error.errors.map(error_ => error_.message));
	t.true(messages.has('first'));
	t.true(messages.has('second'));
});

test('emit() - all listeners run even when one throws', async t => {
	const emitter = new Emittery();
	const executed = [];

	emitter.on('🦄', () => {
		executed.push('first');
		throw new Error('first fails');
	});
	emitter.on('🦄', () => {
		executed.push('second');
	});
	emitter.on('🦄', () => {
		executed.push('third');
	});

	await t.throwsAsync(emitter.emit('🦄'), {instanceOf: AggregateError});
	t.is(executed.length, 3);
});

test('emit() - collects errors from both on() and onAny() listeners', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => {
		throw new Error('regular listener error');
	});
	emitter.onAny(() => {
		throw new Error('any listener error');
	});

	const error = await t.throwsAsync(emitter.emit('🦄'), {instanceOf: AggregateError});
	t.is(error.errors.length, 2);
	const messages = new Set(error.errors.map(error_ => error_.message));
	t.true(messages.has('regular listener error'));
	t.true(messages.has('any listener error'));
});

test('emit() - collects errors from both sync and async throwing listeners', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => {
		throw new Error('sync error');
	});
	emitter.on('🦄', async () => {
		throw new Error('async error');
	});

	const error = await t.throwsAsync(emitter.emit('🦄'), {instanceOf: AggregateError});
	t.is(error.errors.length, 2);
	const messages = new Set(error.errors.map(error_ => error_.message));
	t.true(messages.has('sync error'));
	t.true(messages.has('async error'));
});

test('emitSerial()', async t => {
	const emitter = new Emittery();
	const promise = pEvent(emitter, '🦄');

	const values = [];
	const listener = async value => {
		await delay(Math.random() * 100);
		values.push(value);
	};

	emitter.on('🦄', () => listener(1));
	emitter.on('🦄', () => listener(2));
	emitter.on('🦄', () => listener(3));
	emitter.on('🦄', () => listener(4));
	emitter.on('🦄', () => listener(5));

	await emitter.emitSerial('🦄', 'e');
	await promise;

	t.deepEqual(values, [1, 2, 3, 4, 5]);
});

test('emitSerial() - throws listener error directly (not AggregateError)', async t => {
	const emitter = new Emittery();

	emitter.on('🦄', () => {
		throw new Error('🌈');
	});

	const error = await t.throwsAsync(emitter.emitSerial('🦄'), {instanceOf: Error});
	t.is(error.message, '🌈');
	t.false(error instanceof AggregateError);
});

test('emitSerial() - stops on first listener error', async t => {
	const emitter = new Emittery();
	const executed = [];

	emitter.on('🦄', () => {
		executed.push('first');
		throw new Error('first error');
	});
	emitter.on('🦄', () => {
		executed.push('second');
	});

	await t.throwsAsync(emitter.emitSerial('🦄'), {instanceOf: Error});
	t.deepEqual(executed, ['first']);
});

test('emitSerial() - eventName must be a string, symbol, or number', async t => {
	const emitter = new Emittery();

	emitter.emitSerial('string');
	emitter.emitSerial(Symbol('symbol'));
	emitter.emitSerial(42);

	await t.throwsAsync(emitter.emitSerial(true), {instanceOf: TypeError});
});

test('emitSerial() - userland cannot emit the meta events', async t => {
	const emitter = new Emittery();

	await t.throwsAsync(emitter.emitSerial(Emittery.listenerRemoved), {instanceOf: TypeError});
	await t.throwsAsync(emitter.emitSerial(Emittery.listenerAdded), {instanceOf: TypeError});
});

test('emitSerial() - is async', async t => {
	const emitter = new Emittery();
	const promise = pEvent(emitter, '🦄');

	let unicorn = false;
	emitter.on('🦄', () => {
		unicorn = true;
	});

	emitter.emitSerial('🦄');

	t.false(unicorn);

	await promise;

	t.true(unicorn);
});

test('emitSerial() - calls listeners subscribed when emitSerial() was invoked', async t => {
	const emitter = new Emittery();
	const calls = [];
	const off1 = emitter.on('🦄', () => {
		calls.push(1);
	});
	const p = emitter.emitSerial('🦄');
	emitter.on('🦄', () => {
		calls.push(2);
	});
	await p;
	t.deepEqual(calls, [1]);

	const off3 = emitter.on('🦄', () => {
		calls.push(3);
		off1();
		emitter.on('🦄', () => {
			calls.push(4);
		});
	});
	await emitter.emitSerial('🦄');
	t.deepEqual(calls, [1, 1, 2, 3]);
	off3();

	const off5 = emitter.on('🦄', () => {
		calls.push(5);
		emitter.onAny(() => {
			calls.push(6);
		});
	});
	await emitter.emitSerial('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5]);
	off5();

	let off8 = null;
	emitter.on('🦄', () => {
		calls.push(7);
		off8();
	});
	off8 = emitter.on('🦄', () => {
		calls.push(8);
	});
	await emitter.emitSerial('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6]);

	let off10 = null;
	emitter.onAny(() => {
		calls.push(9);
		off10();
	});
	off10 = emitter.onAny(() => {
		calls.push(10);
	});
	await emitter.emitSerial('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9]);

	await emitter.emitSerial('🦄');
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9, 2, 4, 7, 6, 9]);

	const p2 = emitter.emitSerial('🦄');
	emitter.clearListeners();
	await p2;
	t.deepEqual(calls, [1, 1, 2, 3, 2, 4, 5, 2, 4, 7, 6, 2, 4, 7, 6, 9, 2, 4, 7, 6, 9]);
});

test.serial('emitSerial() - delivers events to events() iterator', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');

	await emitter.emitSerial('🦄', '🌈');
	setTimeout(() => {
		emitter.emitSerial('🦄', Promise.resolve('🌟'));
	}, 10);

	t.plan(3);
	const expected = [{name: '🦄', data: '🌈'}, {name: '🦄', data: '🌟'}];
	for await (const event of iterator) {
		t.deepEqual(event, expected.shift());
		if (expected.length === 0) {
			break;
		}
	}

	t.deepEqual(await iterator.next(), {done: true});
});

test.serial('emitSerial() - delivers explicit undefined payload to events() iterator', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');

	await emitter.emitSerial('🦄', undefined);

	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄', data: undefined}});
	t.true('data' in result.value);
	await iterator.return();
});

test.serial('emitSerial() - delivers events to anyEvent() iterator', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();

	await emitter.emitSerial('🦄', '🌈');
	setTimeout(() => {
		emitter.emitSerial('🦄', Promise.resolve('🌟'));
	}, 10);

	t.plan(3);
	const expected = [{name: '🦄', data: '🌈'}, {name: '🦄', data: '🌟'}];
	for await (const event of iterator) {
		t.deepEqual(event, expected.shift());
		if (expected.length === 0) {
			break;
		}
	}

	t.deepEqual(await iterator.next(), {done: true});
});

test.serial('emitSerial() - delivers explicit undefined payload to anyEvent() iterator', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();

	await emitter.emitSerial('🦄', undefined);

	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄', data: undefined}});
	t.true('data' in result.value);
	await iterator.return();
});

test('emitSerial() - isDebug logs output', async t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.on('test', () => {});
	await emitter.emitSerial('test', 'data');
	t.is(eventStore.length, 2);
	t.is(eventStore[1].type, 'emitSerial');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
	t.is(eventStore[1].eventData, 'data');
});

test('onAny()', async t => {
	t.plan(4);

	const emitter = new Emittery();
	const eventFixture = {foo: true};

	emitter.onAny(({name, data}) => {
		t.is(name, '🦄');
		t.deepEqual(data, eventFixture);
	});

	await emitter.emit('🦄', eventFixture);
	await emitter.emitSerial('🦄', eventFixture);
});

test('onAny() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.onAny(event => resolve(event));
	});
	emitter.emit('🦄');
	const event = await promise;
	t.deepEqual(event, {name: '🦄'});
	t.false('data' in event);
});

test('onAny() - emit explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.onAny(event => resolve(event));
	});
	await emitter.emit('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('onAny() - emitSerial explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const promise = new Promise(resolve => {
		emitter.onAny(event => resolve(event));
	});
	await emitter.emitSerial('🦄', undefined);
	const event = await promise;
	t.deepEqual(event, {name: '🦄', data: undefined});
	t.true('data' in event);
});

test('onAny() - symbol eventName is included in event object', async t => {
	const emitter = new Emittery();
	const eventName = Symbol('test');
	const promise = new Promise(resolve => {
		emitter.onAny(event => resolve(event));
	});
	emitter.emit(eventName, '🌈');
	t.deepEqual(await promise, {name: eventName, data: '🌈'});
});

test('onAny() - receives correct eventName per distinct event', async t => {
	const emitter = new Emittery();
	const events = [];
	emitter.onAny(event => events.push(event));
	await emitter.emit('🦄', '🌈');
	await emitter.emit('🐶', '🍖');
	t.deepEqual(events, [
		{name: '🦄', data: '🌈'},
		{name: '🐶', data: '🍖'},
	]);
});

test('onAny() - must have a listener', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.onAny();
	}, {instanceOf: TypeError});
});

test('onAny() - use abort signal', async t => {
	t.plan(4);

	const emitter = new Emittery();
	const eventFixture = {foo: true};
	const abortController = new AbortController();

	emitter.onAny(({name, data}) => {
		t.is(name, '🦄');
		t.deepEqual(data, eventFixture);
	}, {signal: abortController.signal});

	await emitter.emit('🦄', eventFixture);
	await emitter.emitSerial('🦄', eventFixture);
	abortController.abort();
	await emitter.emit('🦄', eventFixture);
});

test.serial('anyEvent()', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();

	await emitter.emit('🦄', '🌈');
	setTimeout(() => {
		emitter.emit('🦄', Promise.resolve('🌟'));
	}, 10);

	t.plan(3);
	const expected = [{name: '🦄', data: '🌈'}, {name: '🦄', data: '🌟'}];
	for await (const event of iterator) {
		t.deepEqual(event, expected.shift());
		if (expected.length === 0) {
			break;
		}
	}

	t.deepEqual(await iterator.next(), {done: true});
});

test('anyEvent() - dataless event produces event object without data key', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();
	await emitter.emit('🦄');
	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄'}});
	t.false('data' in result.value);
	await iterator.return();
});

test('anyEvent() - explicit undefined payload includes data key', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();
	await emitter.emit('🦄', undefined);
	const result = await iterator.next();
	t.deepEqual(result, {done: false, value: {name: '🦄', data: undefined}});
	t.true('data' in result.value);
	await iterator.return();
});

test('anyEvent() - iterators get isolated event objects', async t => {
	const emitter = new Emittery();
	const firstIterator = emitter.anyEvent();
	const secondIterator = emitter.anyEvent();

	await emitter.emit('🦄', '🌈');
	const first = await firstIterator.next();
	first.value.name = 'changed';
	first.value.data = 'changed';

	const second = await secondIterator.next();
	t.deepEqual(second, {done: false, value: {name: '🦄', data: '🌈'}});

	await firstIterator.return();
	await secondIterator.return();
});

test('anyEvent() - return() called during emit', async t => {
	const emitter = new Emittery();
	let iterator = null;
	emitter.onAny(() => {
		iterator.return();
	});
	iterator = emitter.anyEvent();
	emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});
	t.deepEqual(await iterator.next(), {done: true});
});

test('anyEvent() - discarded iterators should stop receiving events', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {value: {name: '🦄', data: '🌈'}, done: false});
	await iterator.return();
	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: true});

	setTimeout(() => {
		emitter.emit('🦄', '🌟');
	}, 10);

	await new Promise(resolve => {
		setTimeout(resolve, 20);
	});

	t.deepEqual(await iterator.next(), {done: true});
});

test('offAny()', async t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {
		calls.push(1);
	};

	emitter.onAny(listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
	emitter.offAny(listener);
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('offAny() - no listener', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.offAny();
	}, {instanceOf: TypeError});
});

test('clearListeners()', async t => {
	const emitter = new Emittery();
	const calls = [];
	emitter.on('🦄', () => {
		calls.push('🦄1');
	});
	emitter.on('🌈', () => {
		calls.push('🌈');
	});
	emitter.on('🦄', () => {
		calls.push('🦄2');
	});
	emitter.onAny(() => {
		calls.push('any1');
	});
	emitter.onAny(() => {
		calls.push('any2');
	});
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', 'any2', '🌈', 'any1', 'any2']);
	emitter.clearListeners();
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', 'any2', '🌈', 'any1', 'any2']);
});

test('clearListeners() - also clears iterators', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	const anyIterator = emitter.anyEvent();
	await emitter.emit('🦄', '🌟');
	await emitter.emit('🌈', '🌟');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌟'}});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🦄', data: '🌟'}});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🌈', data: '🌟'}});
	await emitter.emit('🦄', '💫');
	emitter.clearListeners();
	await emitter.emit('🌈', '💫');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '💫'}});
	t.deepEqual(await iterator.next(), {done: true});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🦄', data: '💫'}});
	t.deepEqual(await anyIterator.next(), {done: true});
});

test('clearListeners() - with event name', async t => {
	const emitter = new Emittery();
	const calls = [];
	emitter.on('🦄', () => {
		calls.push('🦄1');
	});
	emitter.on('🌈', () => {
		calls.push('🌈');
	});
	emitter.on('🦄', () => {
		calls.push('🦄2');
	});
	emitter.onAny(() => {
		calls.push('any1');
	});
	emitter.onAny(() => {
		calls.push('any2');
	});
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', 'any2', '🌈', 'any1', 'any2']);
	emitter.clearListeners('🦄');
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', 'any2', '🌈', 'any1', 'any2', 'any1', 'any2', '🌈', 'any1', 'any2']);
});

test('clearListeners() - with multiple event names', async t => {
	const emitter = new Emittery();
	const calls = [];
	emitter.on('🦄', () => {
		calls.push('🦄1');
	});
	emitter.on('🌈', () => {
		calls.push('🌈');
	});
	emitter.on('🦄', () => {
		calls.push('🦄2');
	});
	emitter.onAny(() => {
		calls.push('any1');
	});
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', '🌈', 'any1']);
	emitter.clearListeners(['🦄', '🌈']);
	await emitter.emit('🦄');
	await emitter.emit('🌈');
	t.deepEqual(calls, ['🦄1', '🦄2', 'any1', '🌈', 'any1', 'any1', 'any1']);
});

test('clearListeners() - with event name - clears iterators for that event', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');
	const anyIterator = emitter.anyEvent();
	await emitter.emit('🦄', '🌟');
	await emitter.emit('🌈', '🌟');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌟'}});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🦄', data: '🌟'}});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🌈', data: '🌟'}});
	await emitter.emit('🦄', '💫');
	emitter.clearListeners('🦄');
	await emitter.emit('🌈', '💫');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '💫'}});
	t.deepEqual(await iterator.next(), {done: true});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🦄', data: '💫'}});
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🌈', data: '💫'}});
});

test('clearListeners() - isDebug logs output', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.on('test', () => {});
	emitter.clearListeners('test');
	t.is(eventStore.length, 2);
	t.is(eventStore[1].type, 'clear');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
});

test('clearListeners() - debug logger throw does not skip lifecycle deinit cleanup', t => {
	const loggerError = new Error('logger failed');
	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type) {
				if (type === 'clear') {
					throw loggerError;
				}
			},
		},
	});
	let deinitCallCount = 0;
	emitter.init('🦄', () => () => {
		deinitCallCount++;
	});

	emitter.on('🦄', () => {});
	t.throws(() => {
		emitter.clearListeners('🦄');
	}, {is: loggerError});

	t.is(deinitCallCount, 1);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('clearListeners() - anyEvent() works after clearing all listeners', async t => {
	const emitter = new Emittery();
	emitter.clearListeners();

	const iterator = emitter.anyEvent();
	t.is(emitter.listenerCount(), 1);

	await emitter.emit('🦄', '🌟');

	const result = await Promise.race([iterator.next(), delay(50, {value: 'timeout'})]);
	t.not(result, 'timeout');
	t.deepEqual(result, {done: false, value: {name: '🦄', data: '🌟'}});
	await iterator.return();
});

test('onAny() - isDebug logs output', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.onAny(() => {});
	t.is(eventStore.length, 1);
	t.is(eventStore[0].type, 'subscribeAny');
	t.is(eventStore[0].eventName, undefined);
	t.is(eventStore[0].debugName, 'testEmitter');
});

test('offAny() - isDebug logs output', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	const off = emitter.onAny(() => {});
	off();
	t.is(eventStore.length, 2);
	t.is(eventStore[1].type, 'unsubscribeAny');
	t.is(eventStore[1].eventName, undefined);
	t.is(eventStore[1].debugName, 'testEmitter');
});

test('listenerCount()', t => {
	const emitter = new Emittery();
	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.on('🦄', () => {});
	emitter.onAny(() => {});
	emitter.onAny(() => {});
	t.is(emitter.listenerCount('🦄'), 4);
	t.is(emitter.listenerCount('🌈'), 3);
	t.is(emitter.listenerCount(), 5);
});

test('listenerCount() - multiple event names', t => {
	const emitter = new Emittery();
	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.on('🦄', () => {});
	emitter.onAny(() => {});
	emitter.onAny(() => {});
	t.is(emitter.listenerCount(['🦄', '🌈']), 7);
	t.is(emitter.listenerCount(), 5);
});

test('listenerCount() - works with empty eventName strings', t => {
	const emitter = new Emittery();
	emitter.on('', () => {});
	t.is(emitter.listenerCount(''), 1);
});

test('listenerCount() - eventName must be undefined if not a string, symbol, or number', t => {
	const emitter = new Emittery();

	emitter.listenerCount('string');
	emitter.listenerCount(Symbol('symbol'));
	emitter.listenerCount(42);
	emitter.listenerCount();

	t.throws(() => {
		emitter.listenerCount(true);
	}, {instanceOf: TypeError});
});

test('listenerCount() - symbol', t => {
	const symbol = Symbol('🦄');
	const emitter = new Emittery();
	t.is(emitter.listenerCount(symbol), 0);
	emitter.on(symbol, () => {});
	emitter.on(symbol, () => {});
	t.is(emitter.listenerCount(symbol), 2);
	emitter.onAny(() => {});
	emitter.onAny(() => {});
	t.is(emitter.listenerCount(symbol), 4);
});

test('bindMethods()', t => {
	const methodsToBind = ['on', 'off', 'emit', 'listenerCount'];

	const emitter = new Emittery();
	const target = {};

	const oldPropertyNames = Object.getOwnPropertyNames(target);
	emitter.bindMethods(target, methodsToBind);

	t.deepEqual(Object.getOwnPropertyNames(target).sort(), [...oldPropertyNames, ...methodsToBind].sort());

	for (const method of methodsToBind) {
		t.is(typeof target[method], 'function');
	}

	t.is(target.listenerCount(), 0);
});

test('bindMethods() - methodNames must be array of strings or undefined', t => {
	t.throws(() => {
		new Emittery().bindMethods({}, null);
	});

	t.throws(() => {
		new Emittery().bindMethods({}, 'string');
	});

	t.throws(() => {
		new Emittery().bindMethods({}, {});
	});

	t.throws(() => {
		new Emittery().bindMethods({}, [null]);
	});

	t.throws(() => {
		new Emittery().bindMethods({}, [1]);
	});

	t.throws(() => {
		new Emittery().bindMethods({}, [{}]);
	});
});

test('bindMethods() - must bind all methods if no array supplied', t => {
	const methodsExpected = ['on', 'off', 'once', 'events', 'emit', 'emitSerial', 'onAny', 'anyEvent', 'offAny', 'clearListeners', 'init', 'listenerCount', 'bindMethods', 'logIfDebugEnabled'];

	const emitter = new Emittery();
	const target = {};

	const oldPropertyNames = Object.getOwnPropertyNames(target);
	emitter.bindMethods(target);

	t.deepEqual(Object.getOwnPropertyNames(target).sort(), [...oldPropertyNames, ...methodsExpected].sort());

	for (const method of methodsExpected) {
		t.is(typeof target[method], 'function');
	}

	t.is(target.listenerCount(), 0);
});

test('bindMethods() - preserves subclass overrides', async t => {
	let overrideCalled = false;

	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			overrideCalled = true;
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	const target = {};
	emitter.bindMethods(target, ['emit']);

	await target.emit('test', 42);
	t.true(overrideCalled);
});

test('bindMethods() - methodNames must only include Emittery methods', t => {
	const emitter = new Emittery();
	const target = {};

	t.throws(() => {
		emitter.bindMethods(target, ['noexistent']);
	});
});

test('bindMethods() - must not set already existing fields', t => {
	const emitter = new Emittery();
	const target = {
		on: true,
	};

	t.throws(() => {
		emitter.bindMethods(target, ['on']);
	});
});

test('bindMethods() - target must be an object', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.bindMethods('string', []);
	});

	t.throws(() => {
		emitter.bindMethods(null, []);
	});

	t.throws(() => {
		emitter.bindMethods(undefined, []);
	});
});

test('mixin()', t => {
	class TestClass {
		constructor(v) {
			this.v = v;
		}
	}

	const TestClassWithMixin = Emittery.mixin('emitter', ['on', 'off', 'once', 'emit', 'emitSerial', 'onAny', 'offAny', 'clearListeners', 'listenerCount', 'bindMethods'])(TestClass);
	const symbol = Symbol('test symbol');
	const instance = new TestClassWithMixin(symbol);
	t.true(instance.emitter instanceof Emittery);
	t.true(instance instanceof TestClass);
	t.is(instance.emitter, instance.emitter);
	t.is(instance.v, symbol);
	t.is(instance.listenerCount(), 0);
});

test('mixin() - methodNames must be array of strings or undefined', t => {
	class TestClass {}

	t.throws(() => {
		Emittery.mixin('emitter', null)(TestClass);
	});

	t.throws(() => {
		Emittery.mixin('emitter', 'string')(TestClass);
	});

	t.throws(() => {
		Emittery.mixin('emitter', {})(TestClass);
	});

	t.throws(() => {
		Emittery.mixin('emitter', [null])(TestClass);
	});

	t.throws(() => {
		Emittery.mixin('emitter', [1])(TestClass);
	});

	t.throws(() => {
		Emittery.mixin('emitter', [{}])(TestClass);
	});
});

test('mixin() - must mixin all methods if no array supplied', t => {
	const methodsExpected = ['on', 'off', 'once', 'events', 'emit', 'emitSerial', 'onAny', 'anyEvent', 'offAny', 'clearListeners', 'init', 'listenerCount', 'bindMethods', 'logIfDebugEnabled'];

	class TestClass {}

	const TestClassWithMixin = Emittery.mixin('emitter')(TestClass);

	t.deepEqual(Object.getOwnPropertyNames(TestClassWithMixin.prototype).sort(), [...methodsExpected, 'constructor', 'emitter'].sort());
});

test('mixin() - methodNames must only include Emittery methods', t => {
	class TestClass {}

	t.throws(() => {
		Emittery.mixin('emitter', ['nonexistent'])(TestClass);
	});
});

test('mixin() - must not set already existing methods', t => {
	class TestClass {
		on() {
			return true;
		}
	}
	t.throws(() => {
		Emittery.mixin('emitter', ['on'])(TestClass);
	});
});

test('mixin() - target must be function', t => {
	t.throws(() => {
		Emittery.mixin('emitter')('string');
	});

	t.throws(() => {
		Emittery.mixin('emitter')(null);
	});

	t.throws(() => {
		Emittery.mixin('emitter')(undefined);
	});

	t.throws(() => {
		Emittery.mixin('emitter')({});
	});
});

test('isDebug default logger handles symbol event names and object for event data', async t => {
	const emitter = new Emittery({debug: {name: 'testEmitter', enabled: true}});
	const eventName = Symbol('test');
	emitter.on(eventName, () => {});
	await t.notThrowsAsync(emitter.emit(eventName, {complex: ['data', 'structure', 1]}));
});

test('isDebug can be turned on globally during runtime', t => {
	Emittery.isDebugEnabled = true;
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: false,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});

	emitter.on('test', () => {});
	emitter.emit('test', 'test data');
	Emittery.isDebugEnabled = false;
	t.true(eventStore.length > 0);
	t.is(eventStore[1].type, 'emit');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
	t.is(eventStore[1].eventData, 'test data');
});

test('isDebug can be turned on for and instance without using the constructor', t => {
	const eventStore = [];

	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: false,
			logger(type, debugName, eventName, eventData) {
				eventStore.push({
					type,
					debugName,
					eventName,
					eventData,
				});
			},
		},
	});
	emitter.debug.enabled = true;

	emitter.on('test', () => {});
	emitter.emit('test', 'test data');
	t.true(eventStore.length > 0);
	t.is(eventStore[1].type, 'emit');
	t.is(eventStore[1].eventName, 'test');
	t.is(eventStore[1].debugName, 'testEmitter');
	t.is(eventStore[1].eventData, 'test data');
});

test('debug mode - handles circular references in event data', async t => {
	const emitter = new Emittery({
		debug: {
			name: 'testEmitter',
			enabled: true,
		},
	});

	const data = {};
	data.circular = data;

	await t.notThrowsAsync(emitter.emit('test', data));
});

test('subclass emit override is called on instances', async t => {
	let overrideCalled = false;

	class CustomEmittery extends Emittery {
		async emit(eventName, eventData) {
			overrideCalled = true;
			return super.emit(eventName, eventData);
		}
	}

	const emitter = new CustomEmittery();
	let received;
	emitter.on('test', event => {
		received = event;
	});
	await emitter.emit('test', 42);
	t.true(overrideCalled);
	t.deepEqual(received, {name: 'test', data: 42});
});

test('works through a Proxy wrapper', async t => {
	const emitter = new Emittery();
	// Simulate Vue's reactive()/ref() and Alpine.js: they intercept `get` and
	// return methods with `this` bound to the proxy, not the original instance.
	const proxy = new Proxy(emitter, {
		get(target, property, receiver) {
			const value = Reflect.get(target, property, receiver);
			return typeof value === 'function' ? value.bind(receiver) : value;
		},
	});
	const calls = [];

	const off = proxy.on('🦄', () => {
		calls.push('on');
	});
	proxy.onAny(() => {
		calls.push('onAny');
	});
	await proxy.emit('🦄');
	t.deepEqual(calls, ['on', 'onAny']);

	// Unsubscribe via the returned off() function and verify listener is removed
	off();
	await proxy.emit('🦄');
	t.deepEqual(calls, ['on', 'onAny', 'onAny']);

	// Verify once() resolves and auto-unsubscribes through the proxy
	const unicornPromise = proxy.once('🦄');
	await proxy.emit('🦄');
	t.deepEqual(await unicornPromise, {name: '🦄'});
	// Once() listener was removed; only the onAny listener from above remains
	t.is(proxy.listenerCount('🦄'), 1);

	// Verify clearListeners() works through the proxy
	proxy.onAny(() => {});
	proxy.clearListeners();
	t.is(proxy.listenerCount(), 0);
});

test('init() - calls init on first on(), deinit on last off()', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	t.deepEqual(calls, []);

	const off1 = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	const off2 = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']); // No second init

	off1();
	t.deepEqual(calls, ['init']); // No deinit yet

	off2();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - no deinit if initFn returns void', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
	});

	const off = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);
	off();
	t.deepEqual(calls, ['init']); // No deinit
});

test('init() - called immediately if listeners already exist', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.on('🦄', () => {});

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	t.deepEqual(calls, ['init']);
});

test('init() - returns unsubscribe; calling it invokes deinit and removes hooks', t => {
	const emitter = new Emittery();
	const calls = [];

	const removeInit = emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	removeInit(); // Should call deinit and remove the hooks
	t.deepEqual(calls, ['init', 'deinit']);

	// Adding a new listener after removeInit() should NOT call init again
	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - clearListeners() triggers deinit', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	emitter.clearListeners('🦄');
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - clearListeners() with no arg triggers deinit for all events', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		return () => {
			calls.push('deinit:rainbow');
		};
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow']);

	emitter.clearListeners();
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn', 'deinit:rainbow']);
});

test('init() - throws if registered twice for same event', t => {
	const emitter = new Emittery();

	emitter.init('🦄', () => {});

	t.throws(() => {
		emitter.init('🦄', () => {});
	}, {instanceOf: Error});
});

test('init() - throws for meta event names', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.init(Emittery.listenerAdded, () => {});
	}, {instanceOf: TypeError});

	t.throws(() => {
		emitter.init(Emittery.listenerRemoved, () => {});
	}, {instanceOf: TypeError});
});

test('init() - throws if initFn is not a function', t => {
	const emitter = new Emittery();

	t.throws(() => {
		emitter.init('🦄', 'notAFunction');
	}, {instanceOf: TypeError});
});

test('init() - duplicate listener does not trigger init again', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const listener = () => {};
	emitter.on('🦄', listener);
	t.deepEqual(calls, ['init']);

	// Adding the same listener again is a no-op; init must not fire again
	emitter.on('🦄', listener);
	t.deepEqual(calls, ['init']);
});

test('init() - once().off() (manual cancel) triggers deinit', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const promise = emitter.once('🦄');
	t.deepEqual(calls, ['init']);

	// Cancel before the event fires — deinit must run since no listeners remain
	promise.off();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - works with once() (deinit fires when once-listener auto-removes)', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const promise = emitter.once('🦄');
	t.deepEqual(calls, ['init']);

	await emitter.emit('🦄', '🌈');
	await promise;
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - clearListeners() then on() triggers init again', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	emitter.clearListeners('🦄');
	t.deepEqual(calls, ['init', 'deinit']);

	// The lifecycle hook is still registered — a new listener should trigger init again
	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init', 'deinit', 'init']);

	off(); // Off() for an already-cleared listener is a no-op (set doesn't have it)
	t.deepEqual(calls, ['init', 'deinit', 'init']); // Deinit not called again
});

test('init() - can be re-registered after unsubscribing the hook', t => {
	const emitter = new Emittery();
	const calls = [];

	const removeInit = emitter.init('🦄', () => {
		calls.push('init1');
	});

	const off = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init1']);

	removeInit(); // Hook removed; init1 had no deinit

	// Re-register for the same event; fires immediately since a listener is still active
	emitter.init('🦄', () => {
		calls.push('init2');
		return () => {
			calls.push('deinit2');
		};
	});
	t.deepEqual(calls, ['init1', 'init2']);

	off(); // Last listener removed → deinit2 fires
	t.deepEqual(calls, ['init1', 'init2', 'deinit2']);
});

test('init() - works with on() using array of event names', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		return () => {
			calls.push('deinit:rainbow');
		};
	});

	// Single listener subscribed to both events
	const off = emitter.on(['🦄', '🌈'], () => {});
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow']);

	off();
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn', 'deinit:rainbow']);
});

test('init() - abort signal triggers deinit when signal aborts', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const abortController = new AbortController();
	emitter.on('🦄', () => {}, {signal: abortController.signal});
	t.deepEqual(calls, ['init']);

	abortController.abort();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - events() iterator does not trigger lifecycle', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	// Events() registers a producer, not a listener — lifecycle must not fire
	const iterator = emitter.events('🦄');
	t.deepEqual(calls, []);

	await iterator.return();
	t.deepEqual(calls, []); // Deinit also never fires
});

test('init() - initFn throwing during on() rolls back the listener', t => {
	const emitter = new Emittery();
	const error = new Error('init failed');
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		throw error;
	});

	t.throws(() => {
		emitter.on('🦄', () => {});
	}, {is: error});

	t.deepEqual(calls, ['init']);
	t.is(emitter.listenerCount('🦄'), 0); // Listener rolled back
	t.is(eventsMap.get(emitter).get('🦄'), undefined);
});

test('init() - initFn throwing during on() with event name array rolls back earlier subscriptions', t => {
	const emitter = new Emittery();
	const error = new Error('init failed');
	const calls = [];
	const listener = () => {};

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		throw error;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈'], listener);
	}, {is: error});

	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn']);
	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
	t.is(eventsMap.get(emitter).get('🦄'), undefined);
	t.is(eventsMap.get(emitter).get('🌈'), undefined);
});

test('init() - failed on() with event name array keeps pre-existing listener subscriptions', t => {
	const emitter = new Emittery();
	const error = new Error('init failed');
	const listener = () => {};

	emitter.on('🦄', listener);
	emitter.init('🌈', () => {
		throw error;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈'], listener);
	}, {is: error});

	t.is(emitter.listenerCount('🦄'), 1);
	t.true(eventsMap.get(emitter).get('🦄').has(listener));
	t.is(emitter.listenerCount('🌈'), 0);
	t.is(eventsMap.get(emitter).get('🌈'), undefined);
});

test('init() - rollback keeps running and throws original error when deinit throws', t => {
	const emitter = new Emittery();
	const initError = new Error('init failed');
	const deinitError = new Error('deinit failed');
	const listener = () => {};

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.init('🌈', () => () => {});

	emitter.init('🦊', () => {
		throw initError;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈', '🦊'], listener);
	}, {is: initError});

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
	t.is(eventsMap.get(emitter).get('🦄'), undefined);
	t.is(eventsMap.get(emitter).get('🌈'), undefined);
});

test('init() - rollback removes same-listener re-subscription triggered by deinit', t => {
	const emitter = new Emittery();
	const initError = new Error('init failed');
	const listener = () => {};

	emitter.init('🦄', () => () => {
		emitter.on('🦄', listener);
	});

	emitter.init('🌈', () => {
		throw initError;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈'], listener);
	}, {is: initError});

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(eventsMap.get(emitter).get('🦄'), undefined);
});

test('init() - rollback does not emit listenerRemoved for already-removed event entry', async t => {
	const emitter = new Emittery();
	const initError = new Error('init failed');
	const listener = () => {};
	const removedEventNames = [];

	emitter.on(Emittery.listenerRemoved, ({data}) => {
		if (data.eventName) {
			removedEventNames.push(data.eventName);
		}
	});

	emitter.init('🦄', () => () => {
		emitter.off('🌈', listener);
	});

	emitter.init('🌈', () => () => {});

	emitter.init('🦊', () => {
		throw initError;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈', '🦊'], listener);
	}, {is: initError});

	await Promise.resolve();
	t.deepEqual(removedEventNames, ['🌈', '🦄']);
});

test('init() - rollback still emits listenerRemoved when debug logger throws', async t => {
	const initError = new Error('init failed');
	const listener = () => {};
	const removedEventNames = [];
	const emitter = new Emittery({
		debug: {
			enabled: true,
			logger(type) {
				if (type === 'unsubscribe') {
					throw new Error('debug failed');
				}
			},
		},
	});

	emitter.on(Emittery.listenerRemoved, ({data}) => {
		if (data.eventName) {
			removedEventNames.push(data.eventName);
		}
	});

	emitter.init('🦄', () => () => {});
	emitter.init('🌈', () => {
		throw initError;
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈'], listener);
	}, {is: initError});

	await Promise.resolve();
	t.deepEqual(removedEventNames, ['🦄']);
});

test('init() - initFn returning a non-function is silently ignored', t => {
	const emitter = new Emittery();

	emitter.init('🦄', () => 42); // Returns a number, not a function or void

	const off = emitter.on('🦄', () => {});
	t.notThrows(() => off()); // Must not throw — no deinitFn stored
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - immediate init throw does not keep a broken registration', t => {
	const emitter = new Emittery();
	const error = new Error('init failed');

	emitter.on('🦄', () => {});

	t.throws(() => {
		emitter.init('🦄', () => {
			throw error;
		});
	}, {is: error});

	t.notThrows(() => {
		emitter.init('🦄', () => {});
	});
});

test('init() - clearListeners(eventName) runs deinit after listeners are removed', t => {
	const emitter = new Emittery();
	const listenerCountsSeenInDeinit = [];

	emitter.init('🦄', () => () => {
		listenerCountsSeenInDeinit.push(emitter.listenerCount('🦄'));
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.deepEqual(listenerCountsSeenInDeinit, [0]);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - clearListeners(eventName) stays cleared if deinit re-subscribes', t => {
	const emitter = new Emittery();
	let deinitCallCount = 0;

	emitter.init('🦄', () => () => {
		deinitCallCount++;
		emitter.on('🦄', () => {});
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.is(deinitCallCount, 1);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - clearListeners() runs deinit after listeners are removed for each event', t => {
	const emitter = new Emittery();
	const listenerCountsSeenInDeinit = [];

	emitter.init('🦄', () => () => {
		listenerCountsSeenInDeinit.push(['🦄', emitter.listenerCount('🦄')]);
	});

	emitter.init('🌈', () => () => {
		listenerCountsSeenInDeinit.push(['🌈', emitter.listenerCount('🌈')]);
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.clearListeners();

	t.deepEqual(listenerCountsSeenInDeinit, [['🦄', 0], ['🌈', 0]]);
});

test('init() - clearListeners() stays cleared if deinit re-subscribes onAny()', t => {
	const emitter = new Emittery();

	emitter.init('🦄', () => () => {
		emitter.onAny(() => {});
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners();

	t.is(emitter.listenerCount(), 0);
});

test('init() - clearListeners() stays cleared if deinit re-subscribes to a different event', t => {
	const emitter = new Emittery();

	emitter.init('🦄', () => () => {
		emitter.on('🌈', () => {});
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners();

	t.is(emitter.listenerCount(), 0);
	t.false(eventsMap.get(emitter).has('🌈'));
});

test('init() - clearListeners(eventName) does not re-enter deinit via removeInit()', t => {
	const emitter = new Emittery();
	let deinitCallCount = 0;
	const removeInit = emitter.init('🦄', () => () => {
		deinitCallCount++;
		if (deinitCallCount === 1) {
			removeInit();
		}
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.is(deinitCallCount, 1);
});

test('init() - removeInit() does not re-enter deinit cleanup', t => {
	const emitter = new Emittery();
	let deinitCallCount = 0;
	const listener = () => {};

	const removeInit = emitter.init('🦄', () => () => {
		deinitCallCount++;
		if (deinitCallCount === 1) {
			emitter.off('🦄', listener);
		}
	});

	emitter.on('🦄', listener);
	removeInit();

	t.is(deinitCallCount, 1);
});

test('init() - clearListeners(eventName) does not leak deinit emissions to events() iterators', async t => {
	const emitter = new Emittery();
	emitter.init('🦄', () => () => {
		emitter.emit('🦄', 'from-deinit');
	});

	const iterator = emitter.events('🦄');
	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.deepEqual(await iterator.next(), {done: true});
});

test('init() - clearListeners() does not leak deinit emissions to anyEvent() iterators', async t => {
	const emitter = new Emittery();
	emitter.init('🦄', () => () => {
		emitter.emit('🦄', 'from-deinit');
	});

	emitter.on('🦄', () => {});
	const anyIterator = emitter.anyEvent();
	emitter.clearListeners();

	t.deepEqual(await anyIterator.next(), {done: true});
});

test('init() - clearListeners(eventName) blocks deinit emissions for iterators created in deinit', async t => {
	const emitter = new Emittery();
	let iteratorCreatedInDeinit;
	emitter.init('🦄', () => () => {
		iteratorCreatedInDeinit = emitter.events('🦄');
		emitter.emit('🦄', 'from-deinit');
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.truthy(iteratorCreatedInDeinit);
	t.deepEqual(await iteratorCreatedInDeinit.next(), {done: true});
});

test('init() - clearListeners() blocks deinit emissions for anyEvent() iterators created in deinit', async t => {
	const emitter = new Emittery();
	let iteratorCreatedInDeinit;
	emitter.init('🦄', () => () => {
		iteratorCreatedInDeinit = emitter.anyEvent();
		emitter.emit('🦄', 'from-deinit');
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners();

	t.truthy(iteratorCreatedInDeinit);
	t.deepEqual(await iteratorCreatedInDeinit.next(), {done: true});
});

test('init() - removeInit() unregisters lifecycle even if deinit throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	let initCallCount = 0;

	const removeInit = emitter.init('🦄', () => {
		initCallCount++;
		return () => {
			throw deinitError;
		};
	});

	const off = emitter.on('🦄', () => {});
	t.is(initCallCount, 1);

	t.throws(() => {
		removeInit();
	}, {is: deinitError});

	off();
	emitter.on('🦄', () => {});
	t.is(initCallCount, 1);
});

test('init() - clearListeners(eventName) suppression does not block other events', async t => {
	const emitter = new Emittery();
	emitter.init('🦄', () => () => {
		emitter.emit('🌈', 'from-deinit');
	});

	emitter.on('🦄', () => {});
	const anyIterator = emitter.anyEvent();
	emitter.clearListeners('🦄');

	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🌈', data: 'from-deinit'}});
	await anyIterator.return();
});

test('init() - clearListeners(eventName) restores enqueue behavior when deinit throws', async t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.on('🦄', () => {});
	t.throws(() => {
		emitter.clearListeners('🦄');
	}, {is: deinitError});

	const iterator = emitter.events('🦄');
	await emitter.emit('🦄', 'after-throw');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: 'after-throw'}});
	await iterator.return();
});

test('init() - clearListeners() restores enqueue behavior when deinit throws', async t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.on('🦄', () => {});
	t.throws(() => {
		emitter.clearListeners();
	}, {is: deinitError});

	const anyIterator = emitter.anyEvent();
	const rainbowIterator = emitter.events('🌈');
	await emitter.emit('🌈', 'after-throw');
	t.deepEqual(await anyIterator.next(), {done: false, value: {name: '🌈', data: 'after-throw'}});
	t.deepEqual(await rainbowIterator.next(), {done: false, value: {name: '🌈', data: 'after-throw'}});
	await anyIterator.return();
	await rainbowIterator.return();
});

test('init() - clearListeners(eventName) rethrows falsy deinit throw values', t => {
	const emitter = new Emittery();
	const throwValue = value => {
		throw value;
	};

	emitter.init('🦄', () => () => {
		throwValue(0);
	});

	emitter.on('🦄', () => {});
	let thrownError = Symbol('not-thrown');
	try {
		emitter.clearListeners('🦄');
	} catch (error) {
		thrownError = error;
	}

	t.is(thrownError, 0);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - clearListeners(eventName) rethrows undefined deinit throw values', t => {
	const emitter = new Emittery();
	const throwValue = value => {
		throw value;
	};

	emitter.init('🦄', () => () => {
		throwValue(undefined);
	});

	emitter.on('🦄', () => {});
	let thrownError = Symbol('not-thrown');
	try {
		emitter.clearListeners('🦄');
	} catch (error) {
		thrownError = error;
	}

	t.is(thrownError, undefined);
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - clearListeners(eventName) stays authoritative when deinit re-subscribes and throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	emitter.init('🦄', () => () => {
		emitter.on('🦄', () => {});
		throw deinitError;
	});

	emitter.on('🦄', () => {});
	t.throws(() => {
		emitter.clearListeners('🦄');
	}, {is: deinitError});

	t.is(emitter.listenerCount('🦄'), 0);
	t.false(eventsMap.get(emitter).has('🦄'));
});

test('init() - clearListeners() stays authoritative when deinit re-subscribes and throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	emitter.init('🦄', () => () => {
		emitter.on('🦄', () => {});
		throw deinitError;
	});

	emitter.on('🦄', () => {});
	t.throws(() => {
		emitter.clearListeners();
	}, {is: deinitError});

	t.is(emitter.listenerCount('🦄'), 0);
	t.false(eventsMap.get(emitter).has('🦄'));
});

test('init() - clearListeners() stays authoritative when later deinit re-subscribes earlier event and throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	emitter.init('🦄', () => () => {});
	emitter.init('🌈', () => () => {
		emitter.on('🦄', () => {});
		throw deinitError;
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	t.throws(() => {
		emitter.clearListeners();
	}, {is: deinitError});

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
	t.is(emitter.listenerCount(), 0);
	t.false(eventsMap.get(emitter).has('🦄'));
	t.false(eventsMap.get(emitter).has('🌈'));
});

test('init() - clearListeners() continues deinit for later events when earlier deinit throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	let rainbowInitCallCount = 0;
	let rainbowDeinitCallCount = 0;

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.init('🌈', () => {
		rainbowInitCallCount++;
		if (rainbowInitCallCount === 1) {
			return () => {
				rainbowDeinitCallCount++;
			};
		}
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	t.throws(() => {
		emitter.clearListeners();
	}, {is: deinitError});
	t.is(rainbowDeinitCallCount, 1);

	const offRainbow = emitter.on('🌈', () => {});
	offRainbow();

	t.is(rainbowInitCallCount, 2);
	t.is(rainbowDeinitCallCount, 1);
});

test('init() - clearListeners([...]) continues deinit for later events when earlier deinit throws', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');
	let rainbowInitCallCount = 0;
	let rainbowDeinitCallCount = 0;

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.init('🌈', () => {
		rainbowInitCallCount++;
		if (rainbowInitCallCount === 1) {
			return () => {
				rainbowDeinitCallCount++;
			};
		}
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	t.throws(() => {
		emitter.clearListeners(['🦄', '🌈']);
	}, {is: deinitError});
	t.is(rainbowDeinitCallCount, 1);

	const offRainbow = emitter.on('🌈', () => {});
	offRainbow();

	t.is(rainbowInitCallCount, 2);
	t.is(rainbowDeinitCallCount, 1);
});

test('init() - clearListeners([...]) suppresses deinit emissions for each cleared event', async t => {
	const emitter = new Emittery();
	let unicornDeinitCount = 0;
	let rainbowDeinitCount = 0;
	emitter.init('🦄', () => () => {
		unicornDeinitCount++;
		emitter.emit('🦄', 'from-deinit');
	});
	emitter.init('🌈', () => () => {
		rainbowDeinitCount++;
		emitter.emit('🌈', 'from-deinit');
	});

	const unicornIterator = emitter.events('🦄');
	const rainbowIterator = emitter.events('🌈');
	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.clearListeners(['🦄', '🌈']);

	t.is(unicornDeinitCount, 1);
	t.is(rainbowDeinitCount, 1);
	t.deepEqual(await unicornIterator.next(), {done: true});
	t.deepEqual(await rainbowIterator.next(), {done: true});
});

test('init() - clearListeners(eventName) does not leave reinitialized lifecycle active', t => {
	const emitter = new Emittery();
	let activeLifecycleCount = 0;

	emitter.init('🦄', () => {
		activeLifecycleCount++;
		return () => {
			activeLifecycleCount--;
			emitter.on('🦄', () => {});
		};
	});

	emitter.on('🦄', () => {});
	emitter.clearListeners('🦄');

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(activeLifecycleCount, 0);
});

test('init() - clearListeners([...]) suppresses cross-event deinit emissions', async t => {
	const emitter = new Emittery();
	emitter.init('🦄', () => () => {
		emitter.emit('🌈', 'cross-event');
	});

	const rainbowIterator = emitter.events('🌈');
	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.clearListeners(['🦄', '🌈']);

	t.deepEqual(await rainbowIterator.next(), {done: true});
});

test('init() - clearListeners([...]) stays authoritative when later deinit re-subscribes earlier event', t => {
	const emitter = new Emittery();
	emitter.init('🦄', () => () => {});
	emitter.init('🌈', () => () => {
		emitter.on('🦄', () => {});
	});

	emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	emitter.clearListeners(['🦄', '🌈']);

	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
});

test('clearListeners(eventName) - removes eventsMap entry', t => {
	const emitter = new Emittery();
	emitter.on('🦄', () => {});
	t.truthy(eventsMap.get(emitter).has('🦄'));

	emitter.clearListeners('🦄');
	t.false(eventsMap.get(emitter).has('🦄'));
});

test('clearListeners() - handles large event name arrays without stack overflow', t => {
	const emitter = new Emittery();
	const eventNames = Array.from({length: 5000}, (_, index) => `event-${index}`);

	t.notThrows(() => {
		emitter.clearListeners(eventNames);
	});
});

test('init() - removeInit() called twice is safe', t => {
	const emitter = new Emittery();
	let deinitCallCount = 0;

	const removeInit = emitter.init('🦄', () => () => {
		deinitCallCount++;
	});

	emitter.on('🦄', () => {});
	removeInit();
	t.is(deinitCallCount, 1);

	// Second call is a no-op
	removeInit();
	t.is(deinitCallCount, 1);
});

test('init() - removeInit() called twice after re-registration does not delete new lifecycle', t => {
	const emitter = new Emittery();
	const calls = [];

	const removeInit1 = emitter.init('🦄', () => {
		calls.push('init1');
		return () => {
			calls.push('deinit1');
		};
	});

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init1']);

	removeInit1();
	t.deepEqual(calls, ['init1', 'deinit1']);

	// Re-register a new lifecycle for the same event
	emitter.init('🦄', () => {
		calls.push('init2');
		return () => {
			calls.push('deinit2');
		};
	});

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init1', 'deinit1', 'init2']);

	// Calling the OLD removeInit again must NOT delete the new lifecycle
	removeInit1();
	t.deepEqual(calls, ['init1', 'deinit1', 'init2']); // No deinit2

	// Prove the new lifecycle is still active by clearing all listeners
	emitter.clearListeners('🦄');
	t.deepEqual(calls, ['init1', 'deinit1', 'init2', 'deinit2']);
});

test('init() - deinitFn throwing during off() still removes the listener', t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit failed');

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	const listener = () => {};
	emitter.on('🦄', listener);
	t.is(emitter.listenerCount('🦄'), 1);

	t.throws(() => {
		emitter.off('🦄', listener);
	}, {is: deinitError});

	// Listener was removed despite the throw
	t.is(emitter.listenerCount('🦄'), 0);
});

test('init() - works with Symbol event names', t => {
	const emitter = new Emittery();
	const myEvent = Symbol('myEvent');
	const calls = [];

	emitter.init(myEvent, () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off = emitter.on(myEvent, () => {});
	t.deepEqual(calls, ['init']);

	off();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - works with number event names', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init(42, () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off = emitter.on(42, () => {});
	t.deepEqual(calls, ['init']);

	off();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - multiple inits, off() for one event only triggers that deinit', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		return () => {
			calls.push('deinit:rainbow');
		};
	});

	const offUnicorn = emitter.on('🦄', () => {});
	emitter.on('🌈', () => {});
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow']);

	offUnicorn();
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn']);
	// Rainbow deinit NOT called — still has a listener
});

test('init() - listenerAdded meta event still fires when init is registered', async t => {
	const emitter = new Emittery();
	const events = [];

	emitter.on(Emittery.listenerAdded, ({data}) => {
		if (data.eventName === '🦄') {
			events.push('listenerAdded');
		}
	});

	emitter.init('🦄', () => {
		events.push('init');
	});

	emitter.on('🦄', () => {});

	// Init fires synchronously, listenerAdded fires asynchronously
	t.deepEqual(events, ['init']);
	await Promise.resolve();
	t.deepEqual(events, ['init', 'listenerAdded']);
});

test('init() - listenerRemoved meta event still fires when deinit runs', async t => {
	const emitter = new Emittery();
	const events = [];

	emitter.on(Emittery.listenerRemoved, ({data}) => {
		if (data.eventName === '🦄') {
			events.push('listenerRemoved');
		}
	});

	emitter.init('🦄', () => () => {
		events.push('deinit');
	});

	const off = emitter.on('🦄', () => {});
	off();

	// Deinit fires synchronously, listenerRemoved fires asynchronously
	t.deepEqual(events, ['deinit']);
	await Promise.resolve();
	t.deepEqual(events, ['deinit', 'listenerRemoved']);
});

test('init() - async initFn silently discards the resolved cleanup function', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', async () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off = emitter.on('🦄', () => {});
	// An async initFn returns a Promise instance (typeof 'object'),
	// so the resolved cleanup function is never stored as deinitFn.
	t.deepEqual(calls, ['init']);

	// Let the promise settle to confirm the cleanup is truly discarded
	await Promise.resolve();

	off();
	// Deinit is never called even after the promise resolved
	t.deepEqual(calls, ['init']);
});

test('init() - once() with predicate keeps lifecycle active until predicate matches', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const promise = emitter.once('🦄', ({data}) => data === '🌈');
	t.deepEqual(calls, ['init']);

	// Non-matching emit — listener stays, no deinit
	await emitter.emit('🦄', '❌');
	t.deepEqual(calls, ['init']);

	// Matching emit — listener self-removes, deinit fires
	await emitter.emit('🦄', '🌈');
	await promise;
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - works through a Proxy wrapper', t => {
	const emitter = new Emittery();
	const proxy = new Proxy(emitter, {});
	const calls = [];

	proxy.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off = proxy.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	off();
	t.deepEqual(calls, ['init', 'deinit']);
});

test('init() - onAny() does not trigger lifecycle', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const offAny = emitter.onAny(() => {});
	t.deepEqual(calls, []);

	offAny();
	t.deepEqual(calls, []);
});

test('init() - full re-init cycle via off()', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const off1 = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	off1();
	t.deepEqual(calls, ['init', 'deinit']);

	// Second cycle
	const off2 = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init', 'deinit', 'init']);

	off2();
	t.deepEqual(calls, ['init', 'deinit', 'init', 'deinit']);
});

test('init() - once() with multiple event names triggers init for both, deinit for both on fire', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		return () => {
			calls.push('deinit:rainbow');
		};
	});

	const promise = emitter.once(['🦄', '🌈']);
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow']);

	// Firing one event removes the listener from both events
	await emitter.emit('🦄', '🌟');
	await promise;
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn', 'deinit:rainbow']);
});

test('init() - once() cleanup removes all subscriptions when off() throws for one of multiple event names', async t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit boom');

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.init('🌈', () => () => {});

	const promise = emitter.once(['🦄', '🌈']);
	await emitter.emit('🦄');

	await t.throwsAsync(promise, {is: deinitError});
	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);

	promise.off();
	t.is(emitter.listenerCount('🌈'), 0);
});

test('init() - once() cleanup does not leak listeners when off() throws for one of multiple event names', async t => {
	const emitter = new Emittery();
	const deinitError = new Error('deinit boom');

	emitter.init('🦄', () => () => {
		throw deinitError;
	});

	emitter.init('🌈', () => () => {});

	const promise = emitter.once(['🦄', '🌈']);
	await emitter.emit('🦄');

	await t.throwsAsync(promise, {is: deinitError});
	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);

	await emitter.emit('🌈');
	t.is(emitter.listenerCount('🌈'), 0);
});

test('init() - removeInit() with no listeners ever added is a no-op', t => {
	const emitter = new Emittery();
	const calls = [];

	const removeInit = emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	// InitFn was never called, so removeInit should be a clean no-op
	removeInit();
	t.deepEqual(calls, []);
});

test('init() - off() on event with no listeners does not trigger deinit for other events', t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	// Off on a different event should not affect 🦄's lifecycle
	const listener = () => {};
	emitter.off('🌈', listener);
	t.deepEqual(calls, ['init']);
});

test('init() - events() iterator does not prevent deinit when last on() listener removed', async t => {
	const emitter = new Emittery();
	const calls = [];

	emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	const iterator = emitter.events('🦄');
	const off = emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	off();
	// Deinit should fire because the last on() listener was removed,
	// even though an events() iterator still exists
	t.deepEqual(calls, ['init', 'deinit']);

	await iterator.return();
});

test('init() - rollback deinit re-subscription does not leak orphaned deinitFn', t => {
	const emitter = new Emittery();
	const calls = [];
	const listener = () => {};

	emitter.init('🦄', () => {
		calls.push('init:unicorn');
		return () => {
			calls.push('deinit:unicorn');
			emitter.on('🦄', listener);
		};
	});

	emitter.init('🌈', () => {
		calls.push('init:rainbow');
		throw new Error('init failed');
	});

	t.throws(() => {
		emitter.on(['🦄', '🌈'], listener);
	});

	// Init should NOT fire a second time during rollback (suppressed)
	t.deepEqual(calls, ['init:unicorn', 'init:rainbow', 'deinit:unicorn']);
	t.is(emitter.listenerCount('🦄'), 0);
});

// Dispose tests

test('on() - returns a disposable unsubscribe function', async t => {
	const emitter = new Emittery();
	const calls = [];
	const off = emitter.on('🦄', () => {
		calls.push(1);
	});

	t.is(typeof off[Symbol.dispose], 'function');
	t.is(off[Symbol.dispose], off);

	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	off[Symbol.dispose]();
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('onAny() - returns a disposable unsubscribe function', async t => {
	const emitter = new Emittery();
	const calls = [];
	const off = emitter.onAny(() => {
		calls.push(1);
	});

	t.is(typeof off[Symbol.dispose], 'function');
	t.is(off[Symbol.dispose], off);

	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);

	off[Symbol.dispose]();
	await emitter.emit('🦄');
	t.deepEqual(calls, [1]);
});

test('init() - returns a disposable unsubscribe function', t => {
	const emitter = new Emittery();
	const calls = [];

	const off = emitter.init('🦄', () => {
		calls.push('init');
		return () => {
			calls.push('deinit');
		};
	});

	t.is(typeof off[Symbol.dispose], 'function');
	t.is(off[Symbol.dispose], off);

	emitter.on('🦄', () => {});
	t.deepEqual(calls, ['init']);

	off[Symbol.dispose]();
	t.deepEqual(calls, ['init', 'deinit']);
});

// Async dispose tests

test('events() - iterator is async disposable', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄');

	t.is(typeof iterator[Symbol.asyncDispose], 'function');

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});

	await iterator[Symbol.asyncDispose]();
	t.deepEqual(await iterator.next(), {done: true});
});

test('anyEvent() - iterator is async disposable', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent();

	t.is(typeof iterator[Symbol.asyncDispose], 'function');

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});

	await iterator[Symbol.asyncDispose]();
	t.deepEqual(await iterator.next(), {done: true});
});

// Once with signal tests

test('once() - supports signal option', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	const promise = emitter.once('🦄', {signal: abortController.signal});

	abortController.abort();

	await t.throwsAsync(promise, {name: 'AbortError'});
});

test('once() - signal with AbortSignal.timeout()', async t => {
	const emitter = new Emittery();

	const promise = emitter.once('🦄', {signal: AbortSignal.timeout(50)});

	await t.throwsAsync(promise, {name: 'TimeoutError'});
});

test('once() - pre-aborted signal', async t => {
	const emitter = new Emittery();

	const promise = emitter.once('🦄', {signal: AbortSignal.abort()});

	await t.throwsAsync(promise, {name: 'AbortError'});
});

test('once() - signal + predicate combo', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	const promise = emitter.once('data', {
		predicate: ({data}) => data.ok === true,
		signal: abortController.signal,
	});

	await emitter.emit('data', {ok: false});

	abortController.abort();

	await t.throwsAsync(promise, {name: 'AbortError'});
});

test('once() - signal does not interfere when event fires first', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	const promise = emitter.once('🦄', {signal: abortController.signal});

	emitter.emit('🦄', '🌈');

	const result = await promise;
	t.deepEqual(result, {name: '🦄', data: '🌈'});

	// Aborting after resolution should be harmless
	abortController.abort();
});

test('once() - signal cleans up listener on abort', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	const promise = emitter.once('🦄', {signal: abortController.signal});

	t.is(emitter.listenerCount('🦄'), 1);

	abortController.abort();

	await t.throwsAsync(promise, {name: 'AbortError'});

	t.is(emitter.listenerCount('🦄'), 0);
});

test('once() - signal abort rejects even if deinit throws', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	const promise = emitter.once('🦄', {signal: abortController.signal});
	abortController.abort();

	await t.throwsAsync(promise, {name: 'AbortError'});
	t.is(emitter.listenerCount('🦄'), 0);
});

test('once() - signal abort fully unsubscribes multiple event names when one deinit throws', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	emitter.init('🌈', () => () => {});

	const promise = emitter.once(['🦄', '🌈'], {signal: abortController.signal});
	abortController.abort();

	await t.throwsAsync(promise, {name: 'AbortError'});
	t.is(emitter.listenerCount('🦄'), 0);
	t.is(emitter.listenerCount('🌈'), 0);
});

test('once() - off() removes signal listener even if deinit throws', t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const {signal} = abortController;
	let abortListenerCount = 0;
	const addEventListener = signal.addEventListener.bind(signal);
	const removeEventListener = signal.removeEventListener.bind(signal);

	signal.addEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			++abortListenerCount;
		}

		addEventListener(eventName, listener, options);
	};

	signal.removeEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			--abortListenerCount;
		}

		removeEventListener(eventName, listener, options);
	};

	emitter.init('🦄', () => () => {
		throw new Error('deinit boom');
	});

	const promise = emitter.once('🦄', {signal});
	t.is(abortListenerCount, 1);
	t.throws(() => {
		promise.off();
	}, {message: 'deinit boom'});
	t.is(abortListenerCount, 0);
});

test('once() - signal aborted during setup rejects and unsubscribes', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	emitter.init('🦄', () => {
		abortController.abort();
	});

	const promise = emitter.once('🦄', {signal: abortController.signal});

	const state = await Promise.race([
		(async () => {
			try {
				await promise;
				return 'resolved';
			} catch (error) {
				return error.name;
			}
		})(),
		(async () => {
			await delay(100);
			return 'pending';
		})(),
	]);

	t.is(state, 'AbortError');
	t.is(emitter.listenerCount('🦄'), 0);
});

test('once() - matching event resolves before abort from off() cleanup', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();

	emitter.init('🦄', () => () => {
		abortController.abort();
	});

	const promise = emitter.once('🦄', {signal: abortController.signal});
	await emitter.emit('🦄', '🌈');

	t.deepEqual(await promise, {name: '🦄', data: '🌈'});
	t.true(abortController.signal.aborted);
});

test('once() - off() detaches signal abort handling', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const promise = emitter.once('🦄', {signal: abortController.signal});

	promise.off();
	abortController.abort();

	const state = await Promise.race([
		(async () => {
			try {
				await promise;
				return 'resolved';
			} catch {
				return 'rejected';
			}
		})(),
		(async () => {
			await delay(100);
			return 'pending';
		})(),
	]);

	t.is(state, 'pending');
});

// Events with signal tests

test('events() - supports signal option', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const iterator = emitter.events('🦄', {signal: abortController.signal});

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});

	abortController.abort();
	t.deepEqual(await iterator.next(), {done: true});
});

test('events() - pre-aborted signal', async t => {
	const emitter = new Emittery();
	const iterator = emitter.events('🦄', {signal: AbortSignal.abort()});

	t.deepEqual(await iterator.next(), {done: true});
});

test('events() - signal abort unregisters iterator producer', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const iterator = emitter.events('🦄', {signal: abortController.signal});

	abortController.abort();
	t.deepEqual(await iterator.next(), {done: true});
	await t.notThrowsAsync(emitter.emit('🦄', '🌈'));
	await t.notThrowsAsync(emitter.emitSerial('🦄', '🌈'));
});

test('events() - signal cleanup runs when iterator auto-finishes', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const {signal} = abortController;
	let abortListenerCount = 0;
	const addEventListener = signal.addEventListener.bind(signal);
	const removeEventListener = signal.removeEventListener.bind(signal);

	signal.addEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			++abortListenerCount;
		}

		addEventListener(eventName, listener, options);
	};

	signal.removeEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			--abortListenerCount;
		}

		removeEventListener(eventName, listener, options);
	};

	const iterator = emitter.events('🦄', {signal});
	t.is(abortListenerCount, 1);

	emitter.clearListeners('🦄');
	t.is(abortListenerCount, 0);
	t.deepEqual(await iterator.next(), {done: true});
});

// AnyEvent with signal tests

test('anyEvent() - supports signal option', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const iterator = emitter.anyEvent({signal: abortController.signal});

	await emitter.emit('🦄', '🌈');
	t.deepEqual(await iterator.next(), {done: false, value: {name: '🦄', data: '🌈'}});

	abortController.abort();
	t.deepEqual(await iterator.next(), {done: true});
});

test('anyEvent() - pre-aborted signal', async t => {
	const emitter = new Emittery();
	const iterator = emitter.anyEvent({signal: AbortSignal.abort()});

	t.deepEqual(await iterator.next(), {done: true});
});

test('anyEvent() - signal abort unregisters iterator producer', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const iterator = emitter.anyEvent({signal: abortController.signal});

	abortController.abort();
	t.deepEqual(await iterator.next(), {done: true});
	await t.notThrowsAsync(emitter.emit('🦄', '🌈'));
	await t.notThrowsAsync(emitter.emitSerial('🦄', '🌈'));
});

test('anyEvent() - signal cleanup runs when iterator auto-finishes', async t => {
	const emitter = new Emittery();
	const abortController = new AbortController();
	const {signal} = abortController;
	let abortListenerCount = 0;
	const addEventListener = signal.addEventListener.bind(signal);
	const removeEventListener = signal.removeEventListener.bind(signal);

	signal.addEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			++abortListenerCount;
		}

		addEventListener(eventName, listener, options);
	};

	signal.removeEventListener = (eventName, listener, options) => {
		if (eventName === 'abort') {
			--abortListenerCount;
		}

		removeEventListener(eventName, listener, options);
	};

	const iterator = emitter.anyEvent({signal});
	t.is(abortListenerCount, 1);

	emitter.clearListeners();
	t.is(abortListenerCount, 0);
	t.deepEqual(await iterator.next(), {done: true});
});
```

