# 🎯 COMPLETE VISION: DeafAuth + PinkSync Ecosystem
## *The Core of MBTQ.dev Factory*

**foundational identity and accessibility layer** that powers everything. L

---

# 🔐 DEAFAUTH + 🌸 PINKSYNC - THE CORE DUO
## *Identity + Accessibility = Deaf-First Foundation*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MBTQ.DEV FACTORY                                    │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                      CORE SERVICES FACTORY                            │   │
│  │                                                                       │   │
│  │  ┌─────────────────────────┐      ┌─────────────────────────────┐   │   │
│  │  │      DEAFAUTH           │      │         PINKSYNC            │   │   │
│  │  │    (Identity Layer)     │◄────►│    (Accessibility Broker)   │   │   │
│  │  ├─────────────────────────┤      ├─────────────────────────────┤   │   │
│  │  │ • User Management       │      │ • Real-time Sync           │   │   │
│  │  │ • Authentication        │      │ • Provider Broker          │   │   │
│  │  │ • Communication Prefs   │      │ • WebSocket Server         │   │   │
│  │  │ • Hearing Profiles      │      │ • Captioning Gateway       │   │   │
│  │  │ • Visual Alerts         │      │ • ASL Translation          │   │   │
│  │  │ • Session Management    │      │ • Visual Alerts            │   │   │
│  │  └─────────────────────────┘      └─────────────────────────────┘   │   │
│  │              │                              │                        │   │
│  │              └──────────────┬───────────────┘                        │   │
│  │                             ▼                                         │   │
│  │              ┌─────────────────────────────┐                         │   │
│  │              │     TOGETHER THEY POWER     │                         │   │
│  │              │   All Deaf-First Services   │                         │   │
│  │              └─────────────────────────────┘                         │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                    │                                         │
│                                    ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    POWERED SERVICES                                   │   │
│  │                                                                       │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │   │
│  │  │ Job Magician│  │Business Mag.│  │  IEP Pods   │  │ VR4Deaf.org │ │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘ │   │
│  │                                                                       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 COMPLETE DEAFAUTH + PINKSYNC IMPLEMENTATION

### **Directory Structure**
```
C:\Dev\factory\core\
├── auth/                          # DeafAuth
│   ├── api/                       # REST API endpoints
│   │   ├── v1/
│   │   │   ├── auth.js            # Login/logout/register
│   │   │   ├── users.js           # User management
│   │   │   ├── profile.js         # Communication preferences
│   │   │   └── sessions.js        # Session management
│   │   └── v2/                     # Future version
│   ├── models/                     # Data models
│   │   ├── User.js
│   │   ├── CommunicationPrefs.js
│   │   ├── HearingProfile.js
│   │   └── Session.js
│   ├── middleware/                  # Auth middleware
│   │   ├── jwt.js
│   │   ├── rate-limit.js
│   │   └── accessibility.js
│   ├── services/                    # Business logic
│   │   ├── AuthService.js
│   │   ├── UserService.js
│   │   └── TokenService.js
│   ├── utils/                       # Utilities
│   │   ├── password.js
│   │   ├── validation.js
│   │   └── visual-alerts.js
│   ├── migrations/                   # Database migrations
│   ├── tests/                        # Test suite
│   ├── Dockerfile
│   ├── package.json
│   └── README.md
│
└── sync/                           # PinkSync
    ├── api/                         # REST + WebSocket
    │   ├── v1/
    │   │   ├── sync.js              # Sync endpoints
    │   │   ├── providers.js         # Provider management
    │   │   ├── accommodations.js    # User accommodations
    │   │   └── websocket.js         # WebSocket handlers
    ├── websocket/                    # WebSocket server
    │   ├── server.js
    │   ├── rooms.js
    │   ├── events.js
    │   └── handlers/
    │       ├── caption-handler.js
    │       ├── asl-handler.js
    │       └── alert-handler.js
    ├── providers/                    # Accessibility providers
    │   ├── captioning/
    │   │   ├── deepgram.js
    │   │   ├── assemblyai.js
    │   │   ├── ava.js
    │   │   └── otter.js
    │   ├── asl/
    │   │   ├── signall.js
    │   │   ├── slic.js
    │   │   └── handtalk.js
    │   ├── translation/
    │   │   ├── google.js
    │   │   ├── deepl.js
    │   │   └── microsoft.js
    │   └── alerts/
    │       ├── visual.js
    │       └── haptic.js
    ├── models/
    │   ├── Accommodation.js
    │   ├── Provider.js
    │   └── SyncSession.js
    ├── services/
    │   ├── BrokerService.js
    │   ├── ProviderRouter.js
    │   └── FallbackService.js
    ├── utils/
    │   ├── caption-utils.js
    │   ├── asl-utils.js
    │   └── alert-utils.js
    ├── tests/
    ├── Dockerfile
    ├── package.json
    └── README.md
```

---

## 📝 DEAFAUTH - COMPLETE IMPLEMENTATION

### **1. User Model with Deaf-First Attributes**
```javascript
// auth/models/User.js
const mongoose = require('mongoose');

const CommunicationPreferencesSchema = new mongoose.Schema({
  primary: {
    type: String,
    enum: ['asl', 'written', 'lip-reading', 'cued-speech', 'signed-english'],
    default: 'written'
  },
  secondary: [{
    type: String,
    enum: ['asl', 'written', 'lip-reading', 'cued-speech', 'signed-english']
  }],
  aslProficiency: {
    type: String,
    enum: ['fluent', 'intermediate', 'beginner', 'none'],
    default: 'none'
  },
  requiresInterpreter: {
    type: Boolean,
    default: false
  },
  interpreterPreferences: {
    video: { type: Boolean, default: true },
    inPerson: { type: Boolean, default: false },
    preferredGender: { type: String, enum: ['any', 'male', 'female'] }
  },
  captioningPreference: {
    type: String,
    enum: ['auto', 'manual', 'none'],
    default: 'auto'
  },
  captioningLanguages: [String],
  visualAlerts: {
    type: Boolean,
    default: true
  },
  alertTypes: [{
    type: String,
    enum: ['screen-flash', 'light', 'haptic', 'notification']
  }],
  textSize: {
    type: String,
    enum: ['normal', 'large', 'x-large'],
    default: 'normal'
  },
  highContrast: {
    type: Boolean,
    default: false
  }
});

const HearingProfileSchema = new mongoose.Schema({
  level: {
    type: String,
    enum: ['profound', 'severe', 'moderate', 'mild', 'hearing', 'unknown'],
    default: 'unknown'
  },
  ageOfOnset: {
    type: String,
    enum: ['birth', 'early', 'late', 'unknown'],
    default: 'unknown'
  },
  hearingAids: {
    type: Boolean,
    default: false
  },
  hearingAidType: String,
  cochlearImplant: {
    type: Boolean,
    default: false
  },
  implantType: String,
  tinnitus: {
    type: Boolean,
    default: false
  },
  additionalInfo: String
});

const UserSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  password: {
    type: String,
    required: true,
    select: false
  },
  name: {
    first: String,
    last: String,
    preferred: String
  },
  role: {
    type: String,
    enum: ['client', 'counselor', 'interpreter', 'admin', 'agency'],
    default: 'client'
  },
  communicationPreferences: CommunicationPreferencesSchema,
  hearingProfile: HearingProfileSchema,
  
  // VR-specific fields (for agencies)
  vrAgency: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Agency'
  },
  counselorId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  clientId: String, // External ID from VR agency
  
  // Accessibility accommodations
  accommodations: [{
    type: {
      type: String,
      enum: ['interpreter', 'captioning', 'transcription', 'note-taker', 'assistive-tech']
    },
    provider: String,
    startDate: Date,
    endDate: Date,
    status: {
      type: String,
      enum: ['active', 'pending', 'expired']
    }
  }],
  
  // Metadata
  lastLogin: Date,
  loginCount: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Indexes for fast queries
UserSchema.index({ email: 1 });
UserSchema.index({ role: 1 });
UserSchema.index({ 'communicationPreferences.primary': 1 });

module.exports = mongoose.model('User', UserSchema);
```

### **2. Authentication API with Deaf-First Features**
```javascript
// auth/api/v1/auth.js
const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('../../models/User');
const { validateEmail, validatePassword } = require('../../utils/validation');
const { sendVisualAlert } = require('../../utils/visual-alerts');

// POST /api/v1/auth/register - Register new user with deaf-first attributes
router.post('/register', async (req, res) => {
  try {
    const {
      email,
      password,
      name,
      communicationPreferences,
      hearingProfile
    } = req.body;

    // Validate
    if (!validateEmail(email)) {
      return res.status(400).json({ error: 'Invalid email format' });
    }
    if (!validatePassword(password)) {
      return res.status(400).json({ error: 'Password too weak' });
    }

    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(409).json({ error: 'User already exists' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create user with deaf-first attributes
    const user = new User({
      email,
      password: hashedPassword,
      name,
      communicationPreferences: communicationPreferences || {
        primary: 'written',
        visualAlerts: true,
        captioningPreference: 'auto'
      },
      hearingProfile: hearingProfile || {
        level: 'unknown'
      }
    });

    await user.save();

    // Generate JWT
    const token = jwt.sign(
      { userId: user._id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: '7d' }
    );

    // Return user (without password) and token
    res.status(201).json({
      token,
      user: {
        id: user._id,
        email: user.email,
        name: user.name,
        communicationPreferences: user.communicationPreferences,
        hearingProfile: user.hearingProfile,
        role: user.role
      }
    });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ error: 'Registration failed' });
  }
});

// POST /api/v1/auth/login - Login with multi-method support
router.post('/login', async (req, res) => {
  try {
    const { email, password, method = 'password', aslVideo } = req.body;

    // Find user
    const user = await User.findOne({ email }).select('+password');
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    // Handle different auth methods
    let isValid = false;
    
    switch (method) {
      case 'password':
        isValid = await bcrypt.compare(password, user.password);
        break;
      case 'asl-video':
        // Process ASL video verification
        isValid = await verifyASLVideo(aslVideo, user._id);
        break;
      case 'magic-link':
        // Handle magic link verification
        const { token } = req.body;
        isValid = await verifyMagicLink(token, email);
        break;
      default:
        return res.status(400).json({ error: 'Unsupported auth method' });
    }

    if (!isValid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    // Update last login
    user.lastLogin = new Date();
    user.loginCount += 1;
    await user.save();

    // Generate JWT with communication preferences
    const token = jwt.sign(
      {
        userId: user._id,
        email: user.email,
        role: user.role,
        commPrefs: user.communicationPreferences
      },
      process.env.JWT_SECRET,
      { expiresIn: '7d' }
    );

    // Send visual alert for successful login (if enabled)
    if (user.communicationPreferences.visualAlerts) {
      await sendVisualAlert(user._id, {
        type: 'login-success',
        message: 'Successfully logged in',
        timestamp: new Date()
      });
    }

    res.json({
      token,
      user: {
        id: user._id,
        email: user.email,
        name: user.name,
        communicationPreferences: user.communicationPreferences,
        hearingProfile: user.hearingProfile,
        role: user.role,
        accommodations: user.accommodations
      }
    });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ error: 'Login failed' });
  }
});

// GET /api/v1/auth/me - Get current user profile
router.get('/me', async (req, res) => {
  try {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) {
      return res.status(401).json({ error: 'No token provided' });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.userId)
      .select('-password')
      .populate('counselorId', 'name email');

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.json({ user });
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
});

// POST /api/v1/auth/logout - Logout (invalidate session)
router.post('/logout', async (req, res) => {
  try {
    const token = req.headers.authorization?.split(' ')[1];
    
    // Add token to blacklist (implement with Redis)
    if (token) {
      await blacklistToken(token);
    }

    res.json({ success: true, message: 'Logged out successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Logout failed' });
  }
});
```

### **3. Communication Preferences API**
```javascript
// auth/api/v1/profile.js
router.put('/communication-preferences', authMiddleware, async (req, res) => {
  try {
    const userId = req.user.userId;
    const updates = req.body;

    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Update communication preferences
    user.communicationPreferences = {
      ...user.communicationPreferences,
      ...updates
    };
    user.updatedAt = new Date();
    await user.save();

    // Notify PinkSync of preference change
    await notifyPinkSync(userId, 'preferences-updated', user.communicationPreferences);

    res.json({
      success: true,
      communicationPreferences: user.communicationPreferences
    });
  } catch (error) {
    res.status(500).json({ error: 'Update failed' });
  }
});

// GET /api/v1/profile/accessibility-needs - Get user's accessibility needs
router.get('/accessibility-needs', authMiddleware, async (req, res) => {
  try {
    const userId = req.user.userId;
    const user = await User.findById(userId);

    // Combine all accessibility needs
    const needs = {
      communication: user.communicationPreferences,
      hearing: user.hearingProfile,
      accommodations: user.accommodations,
      visualAlerts: user.communicationPreferences.visualAlerts,
      captioning: user.communicationPreferences.captioningPreference !== 'none',
      interpreter: user.communicationPreferences.requiresInterpreter,
      asl: user.communicationPreferences.primary === 'asl'
    };

    res.json({ needs });
  } catch (error) {
    res.status(500).json({ error: 'Failed to get needs' });
  }
});
```

---

## 🌸 PINKSYNC - COMPLETE IMPLEMENTATION

### **1. WebSocket Server for Real-time Sync**
```javascript
// sync/websocket/server.js
const WebSocket = require('ws');
const jwt = require('jsonwebtoken');
const { handleCaptionStream } = require('./handlers/caption-handler');
const { handleASLStream } = require('./handlers/asl-handler');
const { handleAlertStream } = require('./handlers/alert-handler');
const RoomManager = require('./rooms');

class PinkSyncServer {
  constructor(server) {
    this.wss = new WebSocket.Server({ server });
    this.rooms = new RoomManager();
    this.connections = new Map();
    
    this.setupEventHandlers();
  }

  setupEventHandlers() {
    this.wss.on('connection', async (ws, req) => {
      try {
        // Authenticate connection
        const token = req.url.split('token=')[1];
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        
        const connection = {
          ws,
          userId: decoded.userId,
          role: decoded.role,
          commPrefs: decoded.commPrefs,
          rooms: new Set()
        };

        this.connections.set(decoded.userId, connection);
        
        // Send initial connection confirmation
        ws.send(JSON.stringify({
          type: 'connected',
          userId: decoded.userId,
          timestamp: new Date().toISOString()
        }));

        // Handle incoming messages
        ws.on('message', async (data) => {
          try {
            const message = JSON.parse(data);
            await this.handleMessage(decoded.userId, message);
          } catch (error) {
            console.error('Message handling error:', error);
          }
        });

        // Handle disconnect
        ws.on('close', () => {
          this.handleDisconnect(decoded.userId);
        });

      } catch (error) {
        ws.close(1008, 'Authentication failed');
      }
    });
  }

  async handleMessage(userId, message) {
    const connection = this.connections.get(userId);
    if (!connection) return;

    switch (message.type) {
      case 'subscribe':
        await this.handleSubscribe(userId, message);
        break;
      case 'unsubscribe':
        await this.handleUnsubscribe(userId, message);
        break;
      case 'caption-stream':
        await handleCaptionStream(userId, message, this);
        break;
      case 'asl-stream':
        await handleASLStream(userId, message, this);
        break;
      case 'alert':
        await handleAlertStream(userId, message, this);
        break;
      case 'typing':
      case 'presence':
        await this.broadcastToRoom(message.room, {
          type: message.type,
          userId,
          data: message.data
        }, userId);
        break;
      default:
        console.log('Unknown message type:', message.type);
    }
  }

  async handleSubscribe(userId, message) {
    const { room, sessionId } = message;
    const connection = this.connections.get(userId);
    
    if (connection) {
      connection.rooms.add(room);
      await this.rooms.join(room, userId, connection.ws);
      
      // Notify others in room
      this.broadcastToRoom(room, {
        type: 'user-joined',
        userId,
        timestamp: new Date().toISOString()
      }, userId);
    }
  }

  async handleUnsubscribe(userId, message) {
    const { room } = message;
    const connection = this.connections.get(userId);
    
    if (connection) {
      connection.rooms.delete(room);
      await this.rooms.leave(room, userId);
      
      this.broadcastToRoom(room, {
        type: 'user-left',
        userId,
        timestamp: new Date().toISOString()
      }, userId);
    }
  }

  broadcastToRoom(room, message, excludeUserId = null) {
    const clients = this.rooms.getClients(room);
    
    clients.forEach(clientId => {
      if (clientId === excludeUserId) return;
      
      const connection = this.connections.get(clientId);
      if (connection && connection.ws.readyState === WebSocket.OPEN) {
        connection.ws.send(JSON.stringify(message));
      }
    });
  }

  sendToUser(userId, message) {
    const connection = this.connections.get(userId);
    if (connection && connection.ws.readyState === WebSocket.OPEN) {
      connection.ws.send(JSON.stringify(message));
    }
  }

  handleDisconnect(userId) {
    const connection = this.connections.get(userId);
    if (connection) {
      // Leave all rooms
      connection.rooms.forEach(room => {
        this.rooms.leave(room, userId);
        this.broadcastToRoom(room, {
          type: 'user-disconnected',
          userId,
          timestamp: new Date().toISOString()
        });
      });
      
      this.connections.delete(userId);
    }
  }
}

module.exports = PinkSyncServer;
```

### **2. Room Manager for Real-time Collaboration**
```javascript
// sync/websocket/rooms.js
class RoomManager {
  constructor() {
    this.rooms = new Map(); // room -> Set of userIds
    this.userRooms = new Map(); // userId -> Set of rooms
  }

  async join(roomId, userId, ws) {
    if (!this.rooms.has(roomId)) {
      this.rooms.set(roomId, new Set());
    }
    
    this.rooms.get(roomId).add(userId);
    
    if (!this.userRooms.has(userId)) {
      this.userRooms.set(userId, new Set());
    }
    this.userRooms.get(userId).add(roomId);
    
    // Store WebSocket for this user in this room
    if (!this.roomSockets) this.roomSockets = new Map();
    const key = `${roomId}:${userId}`;
    this.roomSockets.set(key, ws);
  }

  async leave(roomId, userId) {
    if (this.rooms.has(roomId)) {
      this.rooms.get(roomId).delete(userId);
      if (this.rooms.get(roomId).size === 0) {
        this.rooms.delete(roomId);
      }
    }
    
    if (this.userRooms.has(userId)) {
      this.userRooms.get(userId).delete(roomId);
    }
    
    const key = `${roomId}:${userId}`;
    this.roomSockets?.delete(key);
  }

  getClients(roomId) {
    return this.rooms.get(roomId) || new Set();
  }

  getUserRooms(userId) {
    return this.userRooms.get(userId) || new Set();
  }

  getSocket(roomId, userId) {
    const key = `${roomId}:${userId}`;
    return this.roomSockets?.get(key);
  }

  async broadcast(roomId, message, excludeUserId = null) {
    const clients = this.getClients(roomId);
    
    for (const userId of clients) {
      if (userId === excludeUserId) continue;
      
      const socket = this.getSocket(roomId, userId);
      if (socket && socket.readyState === 1) { // WebSocket.OPEN
        socket.send(JSON.stringify(message));
      }
    }
  }

  getRoomInfo(roomId) {
    return {
      id: roomId,
      userCount: this.rooms.get(roomId)?.size || 0,
      users: Array.from(this.rooms.get(roomId) || [])
    };
  }

  getAllRooms() {
    const rooms = [];
    for (const [roomId, users] of this.rooms.entries()) {
      rooms.push({
        id: roomId,
        userCount: users.size
      });
    }
    return rooms;
  }
}

module.exports = RoomManager;
```

### **3. Caption Handler with Multiple Providers**
```javascript
// sync/websocket/handlers/caption-handler.js
const { getProvider } = require('../../providers/provider-factory');

async function handleCaptionStream(userId, message, server) {
  const { room, sessionId, audioData, language, provider = 'auto' } = message.data;
  
  try {
    // Select best provider based on availability and quality
    const captionProvider = await selectCaptionProvider(provider, language);
    
    // Send audio to provider
    const captionStream = await captionProvider.streamCaptions({
      audio: audioData,
      language,
      sessionId
    });
    
    // Stream captions back to room
    captionStream.on('caption', (caption) => {
      server.broadcastToRoom(room, {
        type: 'caption',
        sessionId,
        data: {
          text: caption.text,
          timestamp: caption.timestamp,
          confidence: caption.confidence,
          speaker: caption.speaker,
          language: caption.language
        }
      });
    });
    
    // Handle errors
    captionStream.on('error', (error) => {
      server.sendToUser(userId, {
        type: 'caption-error',
        sessionId,
        error: 'Caption provider error, switching to fallback'
      });
      
      // Try fallback provider
      handleFallbackCaption(userId, message, server);
    });
    
  } catch (error) {
    console.error('Caption stream error:', error);
    server.sendToUser(userId, {
      type: 'caption-error',
      sessionId,
      error: 'Failed to start caption stream'
    });
  }
}

async function selectCaptionProvider(preferred, language) {
  const providers = {
    // Primary providers
    deepgram: require('../../providers/captioning/deepgram'),
    assemblyai: require('../../providers/captioning/assemblyai'),
    ava: require('../../providers/captioning/ava'),
    otter: require('../../providers/captioning/otter'),
    
    // Fallbacks
    google: require('../../providers/captioning/google'),
    microsoft: require('../../providers/captioning/microsoft')
  };
  
  if (preferred !== 'auto' && providers[preferred]) {
    return providers[preferred];
  }
  
  // Auto-select based on language and performance
  const providerOrder = ['deepgram', 'assemblyai', 'google', 'microsoft'];
  
  for (const providerName of providerOrder) {
    const provider = providers[providerName];
    if (await provider.isAvailable(language)) {
      return provider;
    }
  }
  
  throw new Error('No caption provider available');
}

async function handleFallbackCaption(userId, message, server) {
  // Simplified fallback using Google's free tier
  const googleProvider = require('../../providers/captioning/google');
  
  try {
    const captionStream = await googleProvider.streamCaptions(message.data);
    
    captionStream.on('caption', (caption) => {
      server.broadcastToRoom(message.data.room, {
        type: 'caption',
        sessionId: message.data.sessionId,
        data: {
          text: caption.text,
          timestamp: caption.timestamp,
          confidence: caption.confidence,
          fallback: true
        }
      });
    });
  } catch (error) {
    server.sendToUser(userId, {
      type: 'caption-error',
      sessionId: message.data.sessionId,
      error: 'All caption providers failed'
    });
  }
}

module.exports = { handleCaptionStream };
```

### **4. ASL Handler with Translation Services**
```javascript
// sync/websocket/handlers/asl-handler.js
async function handleASLStream(userId, message, server) {
  const { room, sessionId, videoData, direction = 'asl-to-text' } = message.data;
  
  try {
    if (direction === 'asl-to-text') {
      await handleASLToText(userId, message, server);
    } else {
      await handleTextToASL(userId, message, server);
    }
  } catch (error) {
    console.error('ASL stream error:', error);
    server.sendToUser(userId, {
      type: 'asl-error',
      sessionId,
      error: 'ASL translation failed'
    });
  }
}

async function handleASLToText(userId, message, server) {
  const { room, sessionId, videoData } = message.data;
  
  // Select ASL recognition provider
  const aslProvider = await getASLProvider();
  
  // Process video frames
  const recognitionStream = await aslProvider.recognizeSigns({
    video: videoData,
    returnText: true
  });
  
  recognitionStream.on('sign', (sign) => {
    server.broadcastToRoom(room, {
      type: 'asl-translation',
      sessionId,
      data: {
        text: sign.text,
        gloss: sign.gloss,
        confidence: sign.confidence,
        timestamp: sign.timestamp
      }
    });
  });
  
  recognitionStream.on('complete', (transcript) => {
    server.broadcastToRoom(room, {
      type: 'asl-complete',
      sessionId,
      data: {
        transcript: transcript.full,
        summary: transcript.summary
      }
    });
  });
}

async function handleTextToASL(userId, message, server) {
  const { room, sessionId, text } = message.data;
  
  // Select ASL avatar provider
  const avatarProvider = await getAvatarProvider();
  
  // Generate sign language video
  const avatarStream = await avatarProvider.generateSigns({
    text,
    avatar: 'default',
    style: 'realistic'
  });
  
  avatarStream.on('frame', (frame) => {
    server.broadcastToRoom(room, {
      type: 'asl-avatar',
      sessionId,
      data: {
        frame: frame.data,
        timestamp: frame.timestamp,
        text: frame.correspondingText
      }
    });
  });
}

async function getASLProvider() {
  const providers = {
    signall: require('../../providers/asl/signall'),
    slic: require('../../providers/asl/slic'),
    handtalk: require('../../providers/asl/handtalk')
  };
  
  // Try providers in order of availability
  for (const [name, provider] of Object.entries(providers)) {
    if (await provider.isAvailable()) {
      return provider;
    }
  }
  
  throw new Error('No ASL provider available');
}

module.exports = { handleASLStream };
```

### **5. Visual Alert Handler**
```javascript
// sync/websocket/handlers/alert-handler.js
async function handleAlertStream(userId, message, server) {
  const { room, sessionId, alertType, message: alertMessage, urgency } = message.data;
  
  // Get user's communication preferences from DeafAuth
  const userPrefs = await getUserPreferences(userId);
  
  // Determine alert methods based on preferences
  const alertMethods = [];
  
  if (userPrefs.visualAlerts) {
    alertMethods.push('screen-flash');
    alertMethods.push('notification');
  }
  
  if (userPrefs.alertTypes?.includes('light')) {
    alertMethods.push('light-alert');
  }
  
  if (userPrefs.alertTypes?.includes('haptic')) {
    alertMethods.push('haptic');
  }
  
  // Send alerts through all methods
  for (const method of alertMethods) {
    switch (method) {
      case 'screen-flash':
        server.broadcastToRoom(room, {
          type: 'visual-alert',
          sessionId,
          data: {
            style: urgency === 'high' ? 'urgent-flash' : 'gentle-flash',
            color: urgency === 'high' ? '#ff0000' : '#ffff00',
            message: alertMessage,
            duration: urgency === 'high' ? 3000 : 1000
          }
        });
        break;
        
      case 'notification':
        server.broadcastToRoom(room, {
          type: 'notification',
          sessionId,
          data: {
            title: 'Alert',
            body: alertMessage,
            icon: urgency === 'high' ? '⚠️' : 'ℹ️',
            requireInteraction: urgency === 'high'
          }
        });
        break;
        
      case 'light-alert':
        // Send to physical light device
        await triggerLightAlert(userId, alertMessage, urgency);
        break;
        
      case 'haptic':
        server.sendToUser(userId, {
          type: 'haptic-feedback',
          sessionId,
          data: {
            pattern: urgency === 'high' ? 'strong' : 'gentle',
            duration: urgency === 'high' ? 1000 : 300
          }
        });
        break;
    }
  }
}

async function getUserPreferences(userId) {
  // Fetch from DeafAuth
  const response = await fetch(`${process.env.DEAFAUTH_URL}/api/v1/profile/accessibility-needs/${userId}`);
  return response.json();
}

async function triggerLightAlert(userId, message, urgency) {
  // Connect to smart light API (Philips Hue, etc.)
  const lightProvider = require('../../providers/alerts/lights');
  await lightProvider.flash({
    userId,
    pattern: urgency === 'high' ? 'rapid' : 'slow',
    color: urgency === 'high' ? '#ff0000' : '#ffff00',
    duration: urgency === 'high' ? 5000 : 2000
  });
}

module.exports = { handleAlertStream };
```

### **6. Provider Factory for Accessibility Services**
```javascript
// sync/providers/provider-factory.js
class ProviderFactory {
  constructor() {
    this.providers = new Map();
    this.healthChecks = new Map();
    this.failoverStrategies = new Map();
    
    this.initializeProviders();
  }

  initializeProviders() {
    // Captioning providers
    this.registerProvider('captioning', 'deepgram', {
      priority: 1,
      languages: ['en', 'es', 'fr', 'de'],
      check: () => require('./captioning/deepgram').healthCheck()
    });
    
    this.registerProvider('captioning', 'assemblyai', {
      priority: 2,
      languages: ['en', 'es', 'fr'],
      check: () => require('./captioning/assemblyai').healthCheck()
    });
    
    this.registerProvider('captioning', 'ava', {
      priority: 3,
      languages: ['en'],
      check: () => require('./captioning/ava').healthCheck()
    });
    
    this.registerProvider('captioning', 'google', {
      priority: 4,
      languages: ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh'],
      check: () => require('./captioning/google').healthCheck()
    });
    
    // ASL providers
    this.registerProvider('asl', 'signall', {
      priority: 1,
      check: () => require('./asl/signall').healthCheck()
    });
    
    this.registerProvider('asl', 'slic', {
      priority: 2,
      check: () => require('./asl/slic').healthCheck()
    });
    
    this.registerProvider('asl', 'handtalk', {
      priority: 3,
      check: () => require('./asl/handtalk').healthCheck()
    });
    
    // Translation providers
    this.registerProvider('translation', 'google', {
      priority: 1,
      languages: 100+,
      check: () => require('./translation/google').healthCheck()
    });
    
    this.registerProvider('translation', 'deepl', {
      priority: 2,
      languages: 20,
      check: () => require('./translation/deepl').healthCheck()
    });
    
    this.registerProvider('translation', 'microsoft', {
      priority: 3,
      languages: 60,
      check: () => require('./translation/microsoft').healthCheck()
    });
  }

  registerProvider(category, name, config) {
    if (!this.providers.has(category)) {
      this.providers.set(category, new Map());
    }
    
    this.providers.get(category).set(name, {
      ...config,
      name,
      category
    });
    
    // Start health checks
    this.startHealthCheck(category, name, config);
  }

  startHealthCheck(category, name, config) {
    const check = async () => {
      try {
        const healthy = await config.check();
        this.updateHealth(category, name, healthy);
      } catch (error) {
        this.updateHealth(category, name, false);
      }
    };
    
    // Check immediately
    check();
    
    // Then every 60 seconds
    const interval = setInterval(check, 60000);
    
    if (!this.healthChecks.has(category)) {
      this.healthChecks.set(category, new Map());
    }
    this.healthChecks.get(category).set(name, interval);
  }

  updateHealth(category, name, healthy) {
    const provider = this.providers.get(category)?.get(name);
    if (provider) {
      provider.healthy = healthy;
      provider.lastCheck = new Date();
    }
  }

  async getBestProvider(category, requirements = {}) {
    const providers = this.providers.get(category);
    if (!providers) {
      throw new Error(`No providers found for category: ${category}`);
    }
    
    // Get all healthy providers
    const healthy = Array.from(providers.entries())
      .filter(([_, config]) => config.healthy !== false)
      .map(([name, config]) => ({ name, ...config }));
    
    if (healthy.length === 0) {
      throw new Error(`No healthy providers for category: ${category}`);
    }
    
    // Apply language filter
    if (requirements.language) {
      const withLanguage = healthy.filter(p => 
        !p.languages || p.languages.includes(requirements.language)
      );
      if (withLanguage.length > 0) {
        return withLanguage.sort((a, b) => a.priority - b.priority)[0];
      }
    }
    
    // Return highest priority
    return healthy.sort((a, b) => a.priority - b.priority)[0];
  }

  async getProvider(category, name) {
    return this.providers.get(category)?.get(name);
  }

  getAllProviders(category) {
    return Array.from(this.providers.get(category)?.entries() || [])
      .map(([name, config]) => ({
        name,
        ...config
      }));
  }
}

module.exports = new ProviderFactory();
```

---

## 🔗 INTEGRATION BETWEEN DEAFAUTH AND PINKSYNC

### **DeafAuth → PinkSync Integration**
```javascript
// auth/services/PinkSyncIntegration.js
class PinkSyncIntegration {
  constructor() {
    this.pinksyncUrl = process.env.PINKSYNC_URL || 'http://sync:3003';
  }

  async notifyUserUpdate(userId, updates) {
    try {
      await fetch(`${this.pinksyncUrl}/api/v1/users/${userId}/sync`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          type: 'user-update',
          updates,
          timestamp: new Date().toISOString()
        })
      });
    } catch (error) {
      console.error('Failed to notify PinkSync:', error);
    }
  }

  async getUserAccommodations(userId) {
    try {
      const response = await fetch(`${this.pinksyncUrl}/api/v1/users/${userId}/accommodations`);
      return response.json();
    } catch (error) {
      return { accommodations: [] };
    }
  }

  async syncUserPreferences(userId) {
    // Get user preferences from DeafAuth
    const user = await User.findById(userId);
    
    // Send to PinkSync
    await fetch(`${this.pinksyncUrl}/api/v1/users/${userId}/preferences`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        communication: user.communicationPreferences,
        hearing: user.hearingProfile,
        accommodations: user.accommodations,
        lastSync: new Date().toISOString()
      })
    });
  }
}
```

### **PinkSync → DeafAuth Integration**
```javascript
// sync/services/DeafAuthIntegration.js
class DeafAuthIntegration {
  constructor() {
    this.deafauthUrl = process.env.DEAFAUTH_URL || 'http://auth:3002';
  }

  async validateToken(token) {
    try {
      const response = await fetch(`${this.deafauthUrl}/api/v1/auth/validate`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      return response.ok ? response.json() : null;
    } catch {
      return null;
    }
  }

  async getUserPreferences(userId) {
    try {
      const response = await fetch(`${this.deafauthUrl}/api/v1/users/${userId}/preferences`);
      return response.json();
    } catch {
      return {
        communicationPreferences: { visualAlerts: true },
        hearingProfile: {}
      };
    }
  }

  async recordAccommodation(userId, accommodation) {
    // Record that accommodation was provided (for VR reporting)
    await fetch(`${this.deafauthUrl}/api/v1/users/${userId}/accommodations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(accommodation)
    });
  }
}
```

---

## 🚀 DEPLOYMENT SCRIPTS

### **Deploy DeafAuth**
```powershell
# C:\Dev\scripts\deploy-deafauth.ps1
cd C:\Dev\factory\core\auth

# Install dependencies
npm install

# Run tests
npm test

# Build Docker image
docker build -t mbtq/deafauth:latest .

# Deploy to environment
docker run -d \
  -p 3002:3002 \
  -e JWT_SECRET=your-secret \
  -e MONGODB_URI=mongodb://localhost:27017/deafauth \
  -e PINKSYNC_URL=http://sync:3003 \
  --name deafauth \
  mbtq/deafauth:latest
```

### **Deploy PinkSync**
```powershell
# C:\Dev\scripts\deploy-pinksync.ps1
cd C:\Dev\factory\core\sync

# Install dependencies
npm install

# Run tests
npm test

# Build Docker image
docker build -t mbtq/pinksync:latest .

# Deploy to environment
docker run -d \
  -p 3003:3003 \
  -e JWT_SECRET=your-secret \
  -e REDIS_URL=redis://localhost:6379 \
  -e DEAFAUTH_URL=http://auth:3002 \
  -e DEEPGRAM_API_KEY=your-key \
  -e ASSEMBLYAI_API_KEY=your-key \
  --name pinksync \
  mbtq/pinksync:latest
```

---

## 📋 WHAT THIS GIVES YOU

### **DeafAuth Provides:**
- ✅ Deaf-first user profiles with communication preferences
- ✅ Multi-method authentication (password, ASL video, magic link)
- ✅ Hearing profiles and accommodation tracking
- ✅ Visual alert preferences
- ✅ JWT tokens with accessibility context

### **PinkSync Provides:**
- ✅ Real-time WebSocket connections
- ✅ Multi-provider captioning (Deepgram, AssemblyAI, Ava, Google)
- ✅ ASL translation (SignAll, SLIC, HandTalk)
- ✅ Visual alert system (screen, lights, haptic)
- ✅ Provider failover and load balancing
- ✅ Room-based collaboration

### **Together They Power:**
- 🔷 **VR4Deaf.org** - Vocational rehabilitation for deaf clients
- 🔷 **Job Magician** - AI-powered job matching with accommodations
- 🔷 **Business Magician** - Business planning with accessibility
- 🔷 **IEP Pods** - Individualized education plans

This is your **foundational core** - everything else in MBTQ.dev builds on top of DeafAuth and PinkSync!
